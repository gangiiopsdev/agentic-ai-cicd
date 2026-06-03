from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Add logic to validate the host
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts