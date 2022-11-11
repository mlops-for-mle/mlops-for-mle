from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
		return {"item_id": item_id}
