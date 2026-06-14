from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Add more sophisticated host validation logic here
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not is_valid_host(sanitized_host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed domains or IP ranges
    return True