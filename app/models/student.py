from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    id:int
    name:str
    email:str
    registered_on:date