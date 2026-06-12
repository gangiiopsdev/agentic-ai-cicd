from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_safe(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', shlex.quote(host)], check=True)

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}