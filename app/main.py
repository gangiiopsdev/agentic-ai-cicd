from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to avoid shell=True
    result = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, universal_newlines=True)
    return {"status": "completed", "output": result}