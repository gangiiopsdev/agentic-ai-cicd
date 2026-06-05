from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def secure_ping(host: str):
    # Use regex to allow only alphanumeric characters and certain punctuation
    if not re.match(r'^[a-zA-Z0-9 .-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}