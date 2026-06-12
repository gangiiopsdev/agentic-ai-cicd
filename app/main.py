from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in ["localhost", "127.0.0.1"]:
        return {"status": "denied"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}