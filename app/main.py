from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "response": "Invalid host"}
    response = safe_ping(host)
    return {"status": "completed", "response": response}
def is_valid_host(host):
    # Simple validation to prevent injection
    return all(c.isalnum() or c in [':', '.', '-', '_'] for c in host)}