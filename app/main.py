from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation with validation, sanitization, and error handling
    if not all(c.isalnum() for c in host) or len(host) > 64:
        raise ValueError("Invalid input")
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to ping host: {e.stderr}")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)