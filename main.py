from contextlib import asynccontextmanager

from fastapi import FastAPI

from Data import Connection
from Models import user
from Routers import users
from Util import hash_password


@asynccontextmanager
async def lifespan(app: FastAPI):
    Connection.Create_db_and_tables()
    print("✅ Database initialized")

    yield  # App is running

    # --- Shutdown ---
    print("👋 App shutting down...")


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "main page"}
