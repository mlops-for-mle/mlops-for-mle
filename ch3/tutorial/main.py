from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
