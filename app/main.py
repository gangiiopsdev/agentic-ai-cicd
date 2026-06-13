from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using Popen and a list of arguments to avoid shell injection
    subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed"}