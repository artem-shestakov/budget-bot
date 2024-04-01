from ..base import Base
from aiogram.filters.callback_data import CallbackData
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class ExpenseCategory(Base):
    title: Mapped[str]
    plan_amount: Mapped[int] = mapped_column(nullable=True)
    budget_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("budget.id"))
