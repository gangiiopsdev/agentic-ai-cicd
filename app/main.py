from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" оформлено как "/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}