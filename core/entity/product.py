from typing import List, Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    unit_price: float
