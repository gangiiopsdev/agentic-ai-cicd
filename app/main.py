from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.strip().isdigit() or len(host) != 3:
        raise ValueError("Invalid host format")
    return execute_ping(host)