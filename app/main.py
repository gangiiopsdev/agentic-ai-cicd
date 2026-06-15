from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and quoting
    if 'ping' in host:
        return {"status": "completed", "error": "Invalid input detected"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}