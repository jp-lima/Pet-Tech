from fastapi import FastAPI
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()


cachorro = {"nome": "fulano"}

@app.get("/")
def root():
    return "status: API rodando"

@app.get("/create-pet")
def create():
    
    return {"status": 200, "response": "cachorro cadastrado com sucesso"}


@app.get("/list-pet")
def list():
    response = supabase.table("PetTech").select("*").execute()
    
    return response

