from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from apis.user import user_router
from apis.place import place_router


kiosk = FastAPI()

kiosk.mount("/static", StaticFiles(directory="static"), name="static")

kiosk.include_router(user_router.router)
kiosk.include_router(place_router.router)