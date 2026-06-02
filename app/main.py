from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only certain IP addresses or domain names
    return host in ['localhost', '127.0.0.1']

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}