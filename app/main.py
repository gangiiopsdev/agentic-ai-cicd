from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to ping host: {e.returncode} - {e.stderr}")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)