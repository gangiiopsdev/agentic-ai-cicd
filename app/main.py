from fastapi import FastAPI
import subprocess
from shlex import quote
globally_banned_hosts = set(['127.0.0.1', '::1'])

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        raise ValueError("Banned host")
    subprocess.run(['ping', quote(host)], shell=False, check=True)
    return {"status": "completed"}