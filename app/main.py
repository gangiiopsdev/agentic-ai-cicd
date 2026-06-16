from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(args):
    sanitized_args = [shlex.quote(arg) for arg in args]
    subprocess.call(sanitized_args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess(['ping', host])
    return {"status": "completed"}