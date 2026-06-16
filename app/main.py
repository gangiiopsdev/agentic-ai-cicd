from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shlex.quote for argument quoting
    if host.strip().isalnum() and '.' in host:
        subprocess.call(["ping", quote(host)])
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}