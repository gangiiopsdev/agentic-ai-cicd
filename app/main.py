from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    return ping(host)