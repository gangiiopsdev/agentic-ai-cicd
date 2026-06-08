from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input to avoid injection attacks
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return "Invalid host"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)