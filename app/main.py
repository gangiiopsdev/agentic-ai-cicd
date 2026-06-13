from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = shlex.split(host)
    result = subprocess.run(['ping'] + args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = shlex.split(host)
    result = subprocess.run(['ping'] + args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}