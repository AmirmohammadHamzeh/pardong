from fastapi import APIRouter, HTTPException, Depends, status
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
async def register(user: MemberModel):
    members_collection = await get_members_collection()
    try:
        await members_collection.insert_one(user.dict())
        return make_response(message="User registered",
                             status_code=status.HTTP_201_CREATED)
    except DuplicateKeyError:
        return make_response(message="user already exists",status_code=status.HTTP_409_CONFLICT)


@router.get("/login/")
async def login(user_id: int):
    members_collection = await get_members_collection()
    existing_user = await members_collection.find_one({"user_id": user_id})

    if not existing_user:
        return make_response(message="User not found", status_code=404)
    token = create_jwt_token(user_id)

    return make_response(message="successful", data={"token": token}, status_code=status.HTTP_202_ACCEPTED)


@router.get("/get_user_data/", summary="Get User Data")
async def protected_route(user_data: dict = Depends(verify_token)):
    members_collection = await get_members_collection()
    existing_user = await members_collection.find_one({"user_id": int(user_data["sub"])})
    if not existing_user:
        return make_response(message="User not found", status_code=status.HTTP_404_NOT_FOUND)
    del existing_user["_id"]
    return make_response(message="successful", data=existing_user, status_code=status.HTTP_200_OK)

