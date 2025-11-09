from fastapi import FastAPI
from supabase import create_client
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Pet(BaseModel):
    nome:str
    idade:int
    status:str
    cpf:str
    especie:str
    raca:str

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode usar ["*"] para permitir tudo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "status: API rodando usaaj"

@app.post("/create-pet")
def create(pet:Pet):
    response =  supabase.table("PetTech").insert({
        "nome":pet.nome,
        "idade":pet.idade,
        "status": pet.status,
        "cpf": pet.cpf,
        }).execute()
    return "adicionado"


@app.get("/list-pet")
def list():
    response = supabase.table("PetTech").select("*").execute()
    
    return response
@app.delete("/delete-pet/{pet_id}")
def delete(pet_id: int):
    response = supabase.table("PetTech").delete().eq("id", pet_id).execute()
    return {"status": 200, "data": response}

@app.put("/update-pet/{pet_id}")
def update(pet_id: int, pet: Pet):
    response = supabase.table("PetTech").update({
        "nome": pet.nome,
        "idade": pet.idade,
        "status": pet.status,
        "cpf": pet.cpf,
        "especie": pet.especie,
        "raca": pet.raca
    }).eq("id", pet_id).execute()
    return {"status": 200, "data": response}

