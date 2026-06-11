from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate host to ensure it's a valid IP address or hostname
        if not validate_host(host):
            raise ValueError('Invalid host')
        subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
def validate_host(host: str) -> bool:
    # Simple validation to ensure the host is not empty and does not contain shell metacharacters
    return all(c.isalnum() or c in '.-' for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}