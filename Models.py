from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class MemberModel(BaseModel):
    user_id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3, max_length=50)
    phone_number: str = Field(..., pattern=r"^09\d{9}$")


class GroupModel(BaseModel):
    group_id: Optional[str] = None
    group_name: str = Field(..., min_length=3, max_length=100)
    owner_id: int = Field(..., gt=0)
    members: List[MemberModel] = Field(..., min_items=1)


# 📌 Expense Collection Model
class ParticipantModel(BaseModel):
    user_id: int = Field(..., gt=0)
    share: int = Field(..., ge=0)
    paid: Optional[bool] = False


class ExpenseModel(BaseModel):
    group_id: Optional[str] = None
    expense_id: Optional[str] = None
    creator_id: Optional[int] = 0
    amount: int = Field(..., gt=0)
    description: str = Field(..., min_length=3, max_length=255)
    timestamp: datetime
    status: Literal["pending", "paid"] = "pending"
    participants: Optional[List] = None
