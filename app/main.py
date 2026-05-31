from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not os.path.exists(host):
        return {"error": "Invalid host"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}