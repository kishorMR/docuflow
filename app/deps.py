import uuid
from collections.abc import AsyncIterator

from fastapi import Header
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import SessionLocal


async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session


async def get_tenant_id(x_tenant_id: uuid.UUID = Header()) -> uuid.UUID:
    return x_tenant_id