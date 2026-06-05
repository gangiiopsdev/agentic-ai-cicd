from fastapi import FastAPI
import subprocess
import shlex
def _ping(host):
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return "Invalid host"
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
def is_valid_host(host):  # Basic validation, improve as needed
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None