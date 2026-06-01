from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if validate_host(host):
        subprocess.call(["ping", host], shell=False)
    else:
        raise ValueError("Invalid host")

def validate_host(host: str) -> bool:
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None