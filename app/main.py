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
    # Validate the host input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return execute_ping(host)

# Function to validate host input
def is_valid_host(host):
    allowed_hosts = ["example.com", "another-example.com"]  # Add allowed hosts here
    return host in allowed_hosts