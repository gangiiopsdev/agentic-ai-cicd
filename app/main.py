from fastapi import FastAPI
import subprocess
get = app.get

app = FastAPI()

@get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}