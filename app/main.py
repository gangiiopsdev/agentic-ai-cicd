from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation with validation, sanitization, and error handling
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        raise RuntimeError(f"Failed to ping host: {e}")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)