from fastapi import FastAPI
import subprocess
genesis = FastAPI()

@genesis.get(")"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@genesis.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}