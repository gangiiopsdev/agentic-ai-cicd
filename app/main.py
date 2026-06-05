from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts