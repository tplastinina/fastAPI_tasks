
from fastapi import FastAPI

from contextlib import asynccontextmanager
from datebase import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):  # именно эта штука создает бд
    await delete_tables()
    print("Datenbank ist sauber")
    await create_tables()
    print("Datenbank ist bereit")
    yield
    print("Aus")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
