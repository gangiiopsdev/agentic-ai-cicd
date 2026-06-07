from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if 'ping' in host or any(char in host for char in [';', '&', '|', '*', '?', '<', '>']):
        return {"error": "Invalid input detected"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}