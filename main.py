from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API Scaffold")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/items/")
async def create_item(item: Item):
    # Add your logic here
    return {"item": item, "created": True}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Add your logic here
    return {"item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)