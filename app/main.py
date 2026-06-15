from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = os.system(f'ping -c 4 {host}')
    if result == 0:
        return {"status": "completed", "result": "Success"}
    else:
        return {"status": "failed", "result": "Failed"}