from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host and not any(char in host for char in [';', '&', '|', '(', ')']):
        subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)