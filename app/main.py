from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_safe_hosts:
        raise ValueError("Invalid host")
    subprocess.call(["ping", f'127.0.0.1'])  # Use a hardcoded safe host instead of user input
    return {"status": "completed"}