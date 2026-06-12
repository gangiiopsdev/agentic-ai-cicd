from fastapi import FastAPI
import subprocess
cimport = subprocess.run,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = cimport(f"ping {host}", shell=False)
    return {"status": "completed", "output": result.stdout}