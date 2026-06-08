from fastapi import FastAPI
import subprocess
c import ping3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not ping3.ping(host, timeout=2):
        return {"status": "failed", "host": host}
    return {"status": "completed", "host": host}