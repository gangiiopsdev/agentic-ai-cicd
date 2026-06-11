from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return "Invalid host"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def is_valid_host(host):
    # Simple validation example
    return all(c.isalnum() or c in ['.', '-'] for c in host)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)