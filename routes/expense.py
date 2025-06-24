from fastapi import APIRouter, Depends, HTTPException, status
# TODO find one faghat yek chiz ro bamigardoone ba find avazesh kon
from Models import ExpenseModel, ParticipantModel
from jwt_token import verify_token
from database import Database
from pymongo.errors import DuplicateKeyError
import uuid
from pymongo import ReturnDocument
from fastapi.encoders import jsonable_encoder
from response_api import make_response


async def get_expense_collection():
    await Database.connect()
    return Database.get_collection("expense")


router = APIRouter()


# TODO maiby some days will change group id
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
        json_compatible_item_data = jsonable_encoder(expense_dict)
        await expense_collection.insert_one(json_compatible_item_data)
        return make_response(message="Expense successfully created", data={"expense_id": expense_id},
                             status_code=status.HTTP_201_CREATED)

    except Exception as e:
        return make_response(message=f"{e}",
                             status_code=status.HTTP_400_BAD_REQUEST)


@router.patch("/add_participants/{expense_id}")
async def add_participants(
        expense_id: str,
        data: ParticipantModel,
        user_data: dict = Depends(verify_token)
):
    expense_collection = await get_expense_collection()
    expense = await expense_collection.find_one({"expense_id": expense_id})

    if not expense:
        return make_response(message="Expense not found",
                             status_code=status.HTTP_404_NOT_FOUND)

    for existing_participant in expense.get("participants", []):
        if str(existing_participant["user_id"]) == data.user_id:
            return make_response(message="Participant already exists", status_code=status.HTTP_409_CONFLICT)

    await expense_collection.update_one({"expense_id": expense_id}, {"$push": {"participants": data.dict()}})

    return make_response(message="Participant added successfully", data={"expense_id": expense_id}
                         , status_code=status.HTTP_200_OK)


@router.patch("/change_paid_true/{expense_id}")
async def mark_paid(expense_id: str, user_data: dict = Depends(verify_token)):
    expense_collection = await get_expense_collection()
    user_id = user_data["sub"]
    updated_expense = await expense_collection.find_one_and_update(
        {"expense_id": expense_id, "participants.user_id": int(user_id)},
        {"$set": {"participants.$.paid": True}},
        return_document=ReturnDocument.AFTER
    )
    if not updated_expense:
        return make_response(message="Expense not found",
                             status_code=status.HTTP_404_NOT_FOUND)

    if all(participant["paid"] for participant in updated_expense["participants"]):
        await expense_collection.update_one({"expense_id": expense_id}, {"$set": {"status": "paid"}})

    return make_response(message="Payment marked as paid successfully",
                         status_code=status.HTTP_200_OK)


# @router.get("/expense_unpaid/")
# async def get_unpaid_expenses(user_data: dict = Depends(verify_token)):
#     expense_collection = await get_expense_collection()
#     user_id = user_data["sub"]
#
#     cursor = expense_collection.find(
#         {
#             "participants": {
#                 "$elemMatch": {
#                     "user_id": int(user_id),
#                     "paid": False
#                 }
#             }
#         }
#     )
#     expenses = await cursor.to_list(length=None)
#
#     if not expenses:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No unpaid expenses found")
#
#     for expense in expenses:
#         expense.pop("_id", None)  # پاک کردن _id از همه رکوردها
#
#     return expenses


@router.get("/get_expense/{expense_id}", description="this api will return expense with that ID")
async def get_group(expense_id: str, user_data: dict = Depends(verify_token)):
    groups_collection = await get_expense_collection()
    expense = await groups_collection.find_one({"expense_id": expense_id})
    if expense is None:
        return make_response(message="Expense not found",
                             status_code=status.HTTP_404_NOT_FOUND)
    del expense["_id"]
    expense["timestamp"] = str(expense["timestamp"])
    print(expense)
    return make_response(message="Expense found", data=expense,
                         status_code=status.HTTP_200_OK)


def convert_object(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@router.get("/expense_unpaid/")
async def get_unpaid_expenses(user_data: dict = Depends(verify_token)):
    expense_collection = await get_expense_collection()
    user_id = user_data["sub"]
    query = {
        "participants": {
            "$elemMatch": {
                "user_id": int(user_id),
                "paid": False
            }
        }
    }

    cursor = expense_collection.find(query)
    results = []
    async for doc in cursor:
        results.append(convert_object(doc))
    if not results:
        return make_response(message="No unpaid charges were found for this user",
                             status_code=status.HTTP_404_NOT_FOUND)
    return make_response(message="The list of group your are in it was successfully retrieved",
                         data={"count": len(results), "data": results}, status_code=status.HTTP_200_OK)
