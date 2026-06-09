from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation with input validation
    output = safe_ping(host)
    return {"status": "completed", "output": output}