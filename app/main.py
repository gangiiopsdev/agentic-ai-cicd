from fastapi import FastAPI
import subprocess
global_params = dict(encoding='utf-8', text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host], **global_params)
    return {"status": "completed"}