from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}