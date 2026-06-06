from fastapi import FastAPI
import subprocess
globally_safe_hosts = {"example.com": True}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_safe_hosts:
        raise Exception('Untrusted host')
    subprocess.call(f'ping {host}', shell=False)
    return {"status": "completed"}