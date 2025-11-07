from fastapi import APIRouter, HTTPException, Depends, status, Query
from pymongo.errors import DuplicateKeyError
from Models import MemberModel
from jwt_token import verify_token, create_jwt_token
from database import Database
from response_api import make_response


async def get_members_collection():
    await Database.connect()
    return Database.get_collection("members")


router = APIRouter()


@router.post("/register/")
async def register_user(user: MemberModel):
    members_collection = await get_members_collection()
    try:
        await members_collection.insert_one(user.dict())
        return make_response(message="User registered",
                             status_code=status.HTTP_201_CREATED)
    except DuplicateKeyError:
        return make_response(message="user already exists", status_code=status.HTTP_409_CONFLICT)


@router.get("/get_user_data/", summary="Get User Data")
async def protected_route(user_id: int = Query(..., description="User_ID")):
    members_collection = await get_members_collection()
    existing_user = await members_collection.find_one({"user_id": user_id})
    if not existing_user:
        return make_response(message="User not found", status_code=status.HTTP_404_NOT_FOUND)
    del existing_user["_id"]
    return make_response(message="successful", data=existing_user, status_code=status.HTTP_200_OK)


@router.get("/check-registration/")
async def check_registration(user_id: int = Query(..., description="User_ID")):
    groups_collection = await get_members_collection()
    user = await groups_collection.find_one({"user_id": user_id})
    if not user:
        return make_response(message="User is not register", status_code=status.HTTP_200_OK)
    return make_response(message="User successfully Found", status_code=status.HTTP_202_ACCEPTED)
