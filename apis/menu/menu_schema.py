from pydantic import BaseModel
from typing import Union, Optional
from fastapi import Form


class MenuSchema(BaseModel):
    name: str
    price: float
    place_id: int
    quantity: int = 1
    out_of_stock: bool

    @classmethod
    def form(
        cls,
        name: str=Form(...),
        price: str=Form(...),
        quantity: Optional[int]=Form(...),
        out_of_stock: Union[str, None] = Form(None)
        ):
        
        out_of_stock = "on" if quantity == 0 else None
        out_of_stock = True if out_of_stock == "on" else False

        return cls(name=name, 
                    price=price, 
                    place_id=0,
                    quantity=quantity, 
                    out_of_stock=out_of_stock
                )