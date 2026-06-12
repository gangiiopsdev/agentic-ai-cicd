from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    # Validate input
    if not host.isalnum() or '..' in host or '.' not in host:
        return "Invalid host"
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)