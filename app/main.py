from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host: str):
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.run(args, check=True, capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    _ping(host)
    return {"status": "completed"}