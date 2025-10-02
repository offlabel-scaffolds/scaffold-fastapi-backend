"""
Items endpoints
Example CRUD operations
"""

from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# In-memory storage (replace with database in production)
items_db = {}

@router.get("/", response_model=List[dict])
async def list_items():
    """List all items"""
    return list(items_db.values())

@router.get("/{item_id}")
async def get_item(item_id: str):
    """Get a specific item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.post("/")
async def create_item(item: dict):
    """Create a new item"""
    item_id = str(len(items_db) + 1)
    items_db[item_id] = {**item, "id": item_id}
    return items_db[item_id]

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    """Delete an item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted"}
