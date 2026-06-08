from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Ensure the host is validated before using it in subprocess
        if not validate_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., regex to check for allowed host patterns)
    return True  # Placeholder for actual validation logic

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}