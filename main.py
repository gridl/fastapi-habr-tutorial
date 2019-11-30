from fastapi import FastAPI
from pydantic import BaseModel
from db import PhraseInput
from db import PhraseOutput
from db import Database

class DeletePhraseResponse(BaseModel):
    success: bool

app = FastAPI(title="Random phrase")
db = Database()

@app.get("/get", response_description="Random phrase", description="Get random phrase from database", response_model=PhraseOutput)
async def get():
    phrase = db.get(db.get_random())
    return phrase

@app.post("/add", response_description="Added phrase with *id* parameter", response_model=PhraseOutput)
async def add(phrase: PhraseInput):
    phrase_out = db.add(phrase)
    return phrase_out

@app.delete("/delete", response_description="Result of deleting", response_model=DeletePhraseResponse)
async def delete(id: int):
    try:
        db.delete(id)
        response = DeletePhraseResponse(success=True)
    except ValueError:
        response = DeletePhraseResponse(success=False)

    return response