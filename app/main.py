from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or not isinstance(host, str) or '&&' in host or ';' in host:
        raise ValueError('Invalid input for ping command')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}