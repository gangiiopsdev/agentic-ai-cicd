from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/"}
def home():
    return {
        "message": "Agentic Self-Healing Pipeline"
    }

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return 'Invalid host'
    return safe_ping(host)