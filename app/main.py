from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"`
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
async def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}