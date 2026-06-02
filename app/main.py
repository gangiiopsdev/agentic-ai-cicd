from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}

    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return host.isdigit() and len(host) == 1