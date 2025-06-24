from fastapi import APIRouter, Depends, HTTPException, status
from Models import GroupModel, MemberModel
from jwt_token import verify_token
from database import Database
from pymongo.errors import DuplicateKeyError
import uuid
from response_api import make_response


def convert_object(doc):
    doc["_id"] = str(doc["_id"])
    return doc


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
        return make_response(message="Group created successfully", data={"group_id": group_id}, status_code=201)
    except DuplicateKeyError:
        return make_response(message="Group ID already exists",
                             status_code=status.HTTP_400_BAD_REQUEST)


@router.patch("/add_member/{group_id}")
async def add_member(group_id: str, member: MemberModel, user_data: dict = Depends(verify_token)):
    groups_collection = await get_group_collection()
    group = await groups_collection.find_one({"group_id": group_id})
    if not group:
        return make_response(message="Group not found", status_code=status.HTTP_404_NOT_FOUND)

    for existing_member in group.get("members", []):
        if existing_member["user_id"] == member.user_id:
            return make_response(message="Member already exists in the group", status_code=status.HTTP_400_BAD_REQUEST)

    await groups_collection.update_one({"group_id": group_id}, {"$push": {"members": member.dict()}})
    return make_response(message="Member added successfully", status_code=status.HTTP_200_OK)


@router.get("/get_group/{group_id}", description="this api will return group with that ID")
async def get_group(group_id: str, user_data: dict = Depends(verify_token)):
    groups_collection = await get_group_collection()
    group = await groups_collection.find_one({"group_id": group_id})
    if group is None:
        return make_response(message="Group not found", data=group, status_code=status.HTTP_404_NOT_FOUND)
    del group["_id"]
    return make_response(message="group successfully found", data=group, status_code=status.HTTP_200_OK)


@router.get("/group_info/")
async def get_group_info(user_data: dict = Depends(verify_token)):
    group_collection = await get_group_collection()
    user_id = user_data["sub"]
    print(user_id)
    query = {
        "members": {
            "$elemMatch": {
                "user_id": int(user_id)
            }
        }
    }

    cursor = group_collection.find(query)
    results = []
    async for doc in cursor:
        results.append(convert_object(doc))
    if not results:
        return make_response(message="No unpaid charges were found for this user",
                             status_code=status.HTTP_404_NOT_FOUND)
    return make_response(message="The list of unpaid expenses was successfully retrieved",
                         data={"count": len(results), "data": results}, status_code=status.HTTP_200_OK)
