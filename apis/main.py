from fastapi import FastAPI
from .routers.user_router import router


kiosk = FastAPI()

kiosk.include_router(router)