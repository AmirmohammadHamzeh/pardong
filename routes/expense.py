from fastapi import APIRouter, Depends, HTTPException, status

from Models import ExpenseModel, ParticipantModel
from jwt_token import verify_token
from database import Database
from pymongo.errors import DuplicateKeyError
import uuid
from pymongo import ReturnDocument


async def get_expense_collection():
    await Database.connect()
    return Database.get_collection("expense")


router = APIRouter()


@router.post("/add_expense/{group_id}", summary="Add Expense")
async def get_group_member(group_id: str, expense: ExpenseModel, user_data: dict = Depends(verify_token)):
    expense_collection = await get_expense_collection()
    expense_id = str(uuid.uuid4())
    expense_dict = expense.dict()
    expense_dict["group_id"] = group_id
    expense_dict["expense_id"] = expense_id
    expense_dict["creator_id"] = int(user_data["sub"])
    expense_dict["participants"] = []
    try:
        await expense_collection.insert_one(expense_dict)
        return HTTPException(status_code=status.HTTP_201_CREATED, detail=f"Expense id:{expense_id}")
    except Exception as e:
        return {f"error{e}"}

