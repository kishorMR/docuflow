from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_session
from app.models import Tenant
from app.schemas import TenantCreate, TenantOut

router = APIRouter(prefix="/tenants", tags=["tenants"])


@router.post("", response_model=TenantOut, status_code=201)
async def create_tenant(
    body: TenantCreate, session: AsyncSession = Depends(get_session)
):
    tenant = Tenant(name=body.name)
    session.add(tenant)
    await session.commit()
    await session.refresh(tenant)
    return tenant