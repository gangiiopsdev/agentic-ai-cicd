from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is safe before using it in the ping command
    if not validate_host(host):
        raise ValueError("Invalid host")
    allowed_hosts = {"example.com", "127.0.0.1"}
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def validate_host(host: str) -> bool:
    # Simple validation example, more complex checks can be added
    allowed_hosts = {"example.com", "127.0.0.1"}
    return host in allowed_hosts