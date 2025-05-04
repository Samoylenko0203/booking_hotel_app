"""
App config
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes import (hotels, rooms, bookings, auth)
from app.db import init_database

@asynccontextmanager
async def lifespan():
    '''
    init db
    '''
    init_database()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Система управления бронированиями в отеле",
    description="Система управления бронированиями в отеле на фреймворке FastAPI",
    version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(hotels.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
app.include_router(auth.router)
