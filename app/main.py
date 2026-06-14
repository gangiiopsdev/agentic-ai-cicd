from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f"ping {host}")
        subprocess.call(args, shell=False)
    except Exception as e:
        return {"error": str(e)}
    
    return {"status": "completed"}