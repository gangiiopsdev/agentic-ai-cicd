from fastapi import FastAPI
import subprocess
import re
def sanitize_host(host):
    return re.sub(r'[^a-zA-Z0-9.-]+', '', host)

app = FastAPI()

global_host = 'example.com' # Ensure this is sanitized

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        raise ValueError("Invalid hostname")

    # Secure implementation
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}