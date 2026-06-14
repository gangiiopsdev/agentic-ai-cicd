from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ["ping", host]
    if not args:
        raise ValueError("No command to execute")
    subprocess.run(args, check=True)
    return {"status": "completed"}