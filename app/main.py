from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host.strip().isdigit() and int(host) >= 1 and int(host) <= 254:
        subprocess.call(["ping", str(host)])
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}