from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from bson import ObjectId
from datetime import datetime


# Helper class for ObjectId conversion
class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


# 📌 Group Collection Model
class MemberModel(BaseModel):
    user_id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3, max_length=50)


class GroupModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    group_id: str = Field(..., min_length=3, max_length=20)
    group_name: str = Field(..., min_length=3, max_length=100)
    owner_id: int = Field(..., gt=0)
    members: List[MemberModel] = Field(..., min_items=1)


# 📌 Expense Collection Model
class ParticipantModel(BaseModel):
    user_id: int = Field(..., gt=0)
    share: int = Field(..., ge=0)
    paid: bool = Field(...)


class ExpenseModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    group_id: str = Field(..., min_length=3, max_length=20)
    expense_id: str = Field(..., min_length=3, max_length=20)
    creator_id: int = Field(..., gt=0)
    amount: int = Field(..., gt=0)  # مبلغ باید مثبت باشد
    description: str = Field(..., min_length=3, max_length=255)
    timestamp: datetime
    status: Literal["pending", "approved", "rejected"] = "pending"
    participants: List[ParticipantModel] = Field(..., min_items=1)


# 📌 Receipts Collection Model
class ReceiptModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    expense_id: str = Field(..., min_length=3, max_length=20)
    payer_id: int = Field(..., gt=0)
    photo_file_id: str = Field(..., min_length=10, max_length=255)
    timestamp: datetime
    status: Literal["waiting_for_approval", "approved", "rejected"] = "waiting_for_approval"