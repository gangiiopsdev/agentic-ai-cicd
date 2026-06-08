from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip() != host or '&&' in host or ';' in host:
        raise ValueError('Invalid input for ping command')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}
    return {"status": "completed"}