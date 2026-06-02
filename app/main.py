from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '-' not in host:
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}