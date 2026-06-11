from fastapi import FastAPI
import subprocess
def execute_ping(host):
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
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return execute_ping(host)

def is_valid_host(host: str) -> bool:
    # Simple validation to ensure the host does not contain special characters or patterns that could be exploited
    return all(c.isalnum() or c in ('.', '-') for c in host)