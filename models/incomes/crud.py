from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.budget import Budget
from .models import ExpenseCategory


async def get_incomes(session: AsyncSession, chat_id: int) -> list[ExpenseCategory]:
    budget_stm = select(Budget).where(Budget.chat_id == chat_id)
    result: Result = await session.execute(budget_stm)
    budget = result.scalar()

    expense_cat_stm = select(ExpenseCategory).where(ExpenseCategory.budget_id == budget.id).order_by(ExpenseCategory.title)
    result: Result = await session.execute(expense_cat_stm)
    products = result.scalars().all()
    return list(products)


async def create_expense_category(session: AsyncSession, expense_cat: ExpenseCategory):
    session.add(expense_cat)
    try:
        await session.commit()
    except IntegrityError as exc:
        print(exc)
    except Exception as exc:
        print(exc)
    return expense_cat