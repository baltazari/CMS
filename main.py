from fastapi import FastAPI

from Routers import Users

from Data import Connection
from Models import User

app = FastAPI()


app.include_router(Users.router)


@app.get("/")
async def root():
    return {"messege": "test"}


@app.on_event("startup")
async def on_startup():
    Connection.Create_db_and_tables()