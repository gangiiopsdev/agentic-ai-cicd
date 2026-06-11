from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host):
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
    return result.stdout
# Add authentication and authorization mechanisms here