from fastapi import FastAPI
from supabase import create_client
import os
from dotenv import load_dotenv
from pydantic import BaseModel


class Pet(BaseModel):
    nome:str
    idade:int
    status:str
    cpf:str

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/")
def root():
    return "status: API rodando"

@app.post("/create-pet")
def create(pet:Pet):
    response =  supabase.table("PetTech").insert({
        "nome":pet.nome,
        "idade":pet.idade,
        "status": pet.status,
        "cpf": pet.cpf,
        "especie": pet.especie,
        "raca": pet.raca
        

        }).execute()
    return {"status": 200, "data": response}


@app.get("/list-pet")
def list():
    response = supabase.table("PetTech").select("*").execute()
    
    return response

