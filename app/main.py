from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and proper argument handling
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

# Preventing command injection by validating host input
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}