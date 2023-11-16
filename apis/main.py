from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from apis.client.user import user_router
from apis.client.place import place_router
from apis.kiosk import kiosk_router


kiosk = FastAPI()

kiosk.mount("/static", StaticFiles(directory="static"), name="static")

kiosk.include_router(user_router.router)
kiosk.include_router(place_router.router)
kiosk.include_router(kiosk_router.router)