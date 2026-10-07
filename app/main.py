from fastapi import FastAPI
from sqlalchemy import text

from app.db import engine
from app.routers import documents, tenants

app = FastAPI(title="DocuFlow")
app.include_router(tenants.router)
app.include_router(documents.router)


@app.get("/health")
async def health():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok"}