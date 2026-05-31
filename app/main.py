from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is safe before using it in the ping command
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

@app.get="/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def validate_host(host: str) -> bool:
    # Simple validation example, more complex checks can be added
    allowed_hosts = ["example.com", "127.0.0.1"]
    return host in allowed_hosts