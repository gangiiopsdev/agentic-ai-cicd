from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple example to validate host format
    return '.' in host

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

    return {"status": "completed", "output": result.stdout.decode()}