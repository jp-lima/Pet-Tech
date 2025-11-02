from pydantic import BaseModel

class Pet(BaseModel):
    nome: str
    idade:int
    status: str
