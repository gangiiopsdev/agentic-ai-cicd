from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and capture_output=True
    if not host or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and capture_output=True
    if not host or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout}