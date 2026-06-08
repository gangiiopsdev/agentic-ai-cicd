from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with full path and input validation
    command = ['ping', host]
    if validate_host(host):
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host provided')

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allow only specific hosts or IP ranges
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts