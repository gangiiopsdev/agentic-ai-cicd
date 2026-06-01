from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or consist only of whitespace')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}