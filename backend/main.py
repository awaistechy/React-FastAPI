import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: List[Fruit]


app = FastAPI()

# Frontend server url | Endpoint
origin = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

memory_DB = {"fruits": []}


@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_DB["fruits"])


@app.post("/fruits")
def add_fruit(fruit: Fruit):
    memory_DB["fruits"].append(fruit)
    return fruit


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
