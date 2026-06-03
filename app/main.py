from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper validation and escaping
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

def is_valid_host(host: str) -> bool:
    # Add validation logic to ensure host is safe and expected
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts