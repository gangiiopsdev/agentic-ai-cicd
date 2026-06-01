from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        # Validate and sanitize the host input
        if not host or not host.isalnum():
            return 'Invalid host'
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)