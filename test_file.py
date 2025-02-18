from fastapi import FastAPI
from pydantic import BaseModel
from common_utils.csvreader import ReadCsv

app = FastAPI()

# Define the request model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# Create a POST endpoint
@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully!", "item": item}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
