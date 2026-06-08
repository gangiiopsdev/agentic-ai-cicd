from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str):
    if not host.strip():
        raise ValueError("Host cannot be empty")
    if ' ' in host:
        raise ValueError("Host should not contain spaces")

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    validate_host(host)
    output = safe_ping(host)
    return {"status": "completed", "output": output}