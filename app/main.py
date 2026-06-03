from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.isalnum() and host.count('.') != 3:
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', '-c 1', f'"{host}"'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}