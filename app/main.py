from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.startswith("-"):
        raise ValueError("Invalid input")
    try:
        response = subprocess.run(["ping", "-c", "1", host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": response.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}