from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    return subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "exit_code": result.returncode}