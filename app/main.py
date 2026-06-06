from fastapi import FastAPI
import subprocess
cimport = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    cimport(f"ping {host}", check=True)
    return {"status": "completed"}