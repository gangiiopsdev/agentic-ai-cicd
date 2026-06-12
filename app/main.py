from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts