from fastapi import APIRouter, Depends, HTTPException, status
from Models import GroupModel, MemberModel
from jwt_token import verify_token
from database import Database
from pymongo.errors import DuplicateKeyError
import uuid


async def get_group_collection():
    await Database.connect()
    return Database.get_collection("group")


async def get_members_collection():
    await Database.connect()
    return Database.get_collection("members")


router = APIRouter()


@router.post("/register")
async def register_group(group: GroupModel, user_data: dict = Depends(verify_token)):
    groups_collection = await get_group_collection()
    group_id = str(uuid.uuid4())
    group_dict = group.dict()
    group_dict["group_id"] = group_id
    try:
        await groups_collection.insert_one(group_dict)
        return {"message": "Group created successfully", "group_id": group_id}
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group ID already exists")


@router.post("/add_member/{group_id}")
async def add_member(group_id: str, member: MemberModel, user_data: dict = Depends(verify_token)):
    groups_collection = await get_group_collection()
    group = await groups_collection.find_one({"group_id": group_id})
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")

    for existing_member in group.get("members", []):
        if existing_member["user_id"] == member.user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Member already exists in the group")

    await groups_collection.update_one({"group_id": group_id}, {"$push": {"members": member.dict()}})
    return {"message": "Member added successfully"}


@router.post("/get_group_member/{group_id}")
async def get_group_member(group_id: str, user_data: dict = Depends(verify_token)):
    groups_collection = await get_group_collection()
    group = await groups_collection.find_one({"group_id": group_id})
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group["members"]
