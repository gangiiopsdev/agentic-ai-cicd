from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host to prevent command injection
    if not is_valid_host(host):
        return 'Invalid host'
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    import re
    allowed_chars = r'^[a-zA-Z0-9.-]+$'
    return re.match(allowed_chars, host) is not None