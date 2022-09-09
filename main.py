import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from dotenv import load_dotenv

from app.routers import books

load_dotenv()
db_url = os.environ.get("DB_URL")

app = FastAPI()
app.include_router(books.router)

app.add_middleware(DBSessionMiddleware, db_url=db_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)