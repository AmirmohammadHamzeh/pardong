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


@router.post("/add_participants/{expense_id}")
async def add_participants(
        expense_id: str,
        data: ParticipantModel,
        user_data: dict = Depends(verify_token)
):
    expense_collection = await get_expense_collection()
    expense = await expense_collection.find_one({"expense_id": expense_id})

    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

    for existing_participant in expense.get("participants", []):
        if existing_participant["user_id"] == data.user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Participant already exists")

    await expense_collection.update_one({"expense_id": expense_id}, {"$push": {"participants": data.dict()}})

    return {"message": "Participant added successfully"}


@router.post("/change_paid_true/{expense_id}")
async def mark_paid(expense_id: str, user_data: dict = Depends(verify_token)):
    expense_collection = await get_expense_collection()
    user_id = user_data["sub"]
    updated_expense = await expense_collection.find_one_and_update(
        {"expense_id": expense_id, "participants.user_id": int(user_id)},
        {"$set": {"participants.$.paid": True}},
        return_document=ReturnDocument.AFTER
    )
    if not updated_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

    if all(participant["paid"] for participant in updated_expense["participants"]):
        await expense_collection.update_one({"expense_id": expense_id}, {"$set": {"status": "paid"}})

    return {"message": "Payment marked as paid successfully"}

