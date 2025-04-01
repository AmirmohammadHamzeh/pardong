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
