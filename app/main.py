from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call for better control and security
        process = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": process.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    return ping(host)

# Function to validate the host
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex matching allowed hosts
    return host.isalnum() and '.' in host