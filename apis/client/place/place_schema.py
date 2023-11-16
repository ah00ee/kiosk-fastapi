from pydantic import BaseModel

from fastapi import Form


class PlaceSchema(BaseModel):
    name: str
    address: str

    @classmethod
    def form(
        cls,
        name: str=Form(...),
        address: str=Form(...)
    ):
        return cls(name=name, address=address)