from fastapi import FastAPI, HTTPException
import subprocess
def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Input contains non-alphanumeric characters")

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        subprocess.run(['ping', '-c 1', host], check=True, shell=False)
        return {"status": "completed"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))