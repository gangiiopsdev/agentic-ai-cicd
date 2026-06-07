from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f'ping {escaped_host}')
    return {"status": "completed"}