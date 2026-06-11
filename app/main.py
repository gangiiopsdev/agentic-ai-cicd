from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)