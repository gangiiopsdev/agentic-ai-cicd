from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return safe_ping(host)

def validate_host(host):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts