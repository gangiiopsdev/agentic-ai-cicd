from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host is sanitized to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host provided")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return True  # Placeholder for actual validation logic