from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": subprocess.run(['ping', host], capture_output=True, text=True).stdout}