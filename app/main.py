from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    # Safer implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

# Define a function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed domains or IP ranges
    return True