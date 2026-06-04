from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate the host input to prevent injection attacks
    if not host.strip().replace('.', '').isnumeric():
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)