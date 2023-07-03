"""
Modul yang memuat pendefinisian item dengan atribut nama item(name), jumlah item (qty), harga item (price). 
"""

from dataclasses import dataclass
@dataclass
class Item:
    name: str
    qty: int
    price: int