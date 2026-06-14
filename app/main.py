from fastapi import FastAPI
import subprocess
global_args = ["ping", "{host}"]
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(global_args)
    return {"status": "completed"}