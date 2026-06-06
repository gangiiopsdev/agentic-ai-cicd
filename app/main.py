from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e == '.').strip()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '.' in sanitized_host:
        subprocess.call(["ping", sanitized_host], shell=False)
    else:
        return {"status": "invalid input"}
    return {"status": "completed"}