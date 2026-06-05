from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Sanitize the host input using shlex.quote to prevent command injection
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return safe_ping(host)