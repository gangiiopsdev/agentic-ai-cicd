from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ["ping", *shlex.split(host)]
    subprocess.run(args, check=True, timeout=5)
    return {"status": "completed"}