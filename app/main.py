from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    # Safe implementation using subprocess.run with list of arguments and shell=False
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)