from fastapi import FastAPI
import subprocess
glitchy_sanitize = lambda x: ''.join(e for e in x if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = glitchy_sanitize(host)
    subprocess.call(f'ping {sanitized_host}')
    return {"status": "completed"}