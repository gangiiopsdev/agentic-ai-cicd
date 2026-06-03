from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True and proper validation of host
    if host.strip() and all(c.isalnum() or c in '-._' for c in host):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed: {e}')
    else:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)