"""
API v1 Router
Aggregates all endpoint routers
"""

from fastapi import APIRouter
from app.api.v1.endpoints import items

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(items.router, prefix="/items", tags=["items"])
