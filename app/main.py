from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.split to safely split the command into a list of arguments
        args = shlex.split('ping ' + host)
        subprocess.call(args)
    except Exception as e:
        return {"error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)