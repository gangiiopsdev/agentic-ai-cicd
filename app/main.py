from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}

    try:
        result = subprocess.run(shlex.split(f"ping {host}"), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}


def is_valid_host(host: str) -> bool:
    # Basic validation to ensure host does not contain potentially harmful characters
    return all(char.isalnum() or char in ('.', '-') for char in host)