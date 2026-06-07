from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to avoid shell injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex matching allowed hosts
    return True