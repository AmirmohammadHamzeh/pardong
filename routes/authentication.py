from fastapi import APIRouter, HTTPException, Depends
from pymongo.errors import DuplicateKeyError
from Models import MemberModel
from jwt_token import verify_token, create_jwt_token
from database import Database


async def get_members_collection():
    await Database.connect()
    return Database.get_collection("members")


router = APIRouter()


@router.post("/register/")
async def register(user: MemberModel):
    members_collection = await get_members_collection()
    try:
        await members_collection.insert_one(user.dict())
        return {"message": "User registered successfully"}
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="User ID already exists")


@router.get("/login/")
async def login(user_id: int):
    members_collection = await get_members_collection()
    existing_user = await members_collection.find_one({"user_id": user_id})

    if not existing_user:
        raise HTTPException(status_code=401, detail="User not found")

    token = create_jwt_token(user_id)
    return {"token": token}


