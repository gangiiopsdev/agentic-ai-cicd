from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Implement your validation logic here, e.g., allow only specific IP ranges or domain names
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts