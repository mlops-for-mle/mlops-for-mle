# main.py
from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
