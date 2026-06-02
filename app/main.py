from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = quote(host)
    subprocess.run(["ping", safe_host], shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}