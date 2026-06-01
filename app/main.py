from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation, sanitization, and error handling
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    try:
        subprocess.call(['ping', shlex.quote(host)], shell=False)
    except Exception as e:
        raise RuntimeError(f"Failed to ping host: {e}")
    return {"status": "completed"}