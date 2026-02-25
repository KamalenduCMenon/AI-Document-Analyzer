from fastapi import FastAPI
from app.services.vertex_service import analyze_document
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/analyze")
def analyze(text: str):
    result = analyze_document(text)
    return {"analysis": result}