from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Any
from datetime import datetime, timezone


class MemberModel(BaseModel):
    user_id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3, max_length=50)
    phone_number: str = Field(..., pattern=r"^09\d{9}$")
    bank_card_number: int = Field(..., gt=0)


class GroupModel(BaseModel):
    group_id: Optional[str] = None
    group_name: str = Field(..., min_length=3, max_length=100)
    owner_id: int = Field(..., gt=0)
    members: List[MemberModel] = Field(..., min_items=1)


class ParticipantModel(BaseModel):
    user_id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3, max_length=50)
    share: int = Field(..., ge=0)
    paid: Optional[bool] = False


class ExpenseModel(BaseModel):
    group_id: str = Field(..., min_length=3, max_length=100)
    expense_id: Optional[str] = None
    creator_id: Optional[int] = 0
    amount: int = Field(..., gt=0)
    description: str = Field(..., min_length=3, max_length=255)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Literal["pending", "paid"] = "pending"
    participants: Optional[List] = None


class ReturnModel(BaseModel):
    status: bool
    message: Optional[str] = None
    data: Optional[Any] = None
