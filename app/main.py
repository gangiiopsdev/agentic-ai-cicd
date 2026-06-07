from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = escape_host(host)
    subprocess.call(f"ping {host}")
    return {"status": "completed"}