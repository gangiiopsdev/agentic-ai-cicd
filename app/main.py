from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        raise ValueError("Invalid hostname")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}