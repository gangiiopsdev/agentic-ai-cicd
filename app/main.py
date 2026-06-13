from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic here, e.g., check if the host is in a predefined list of allowed hosts
    return True

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}