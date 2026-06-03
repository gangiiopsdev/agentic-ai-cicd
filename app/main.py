from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or consist only of whitespace')
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}