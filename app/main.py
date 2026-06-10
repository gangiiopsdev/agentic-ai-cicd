from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host")
    return execute_ping(host)