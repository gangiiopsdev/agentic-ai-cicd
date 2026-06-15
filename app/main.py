from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip() or '..' in host:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        validate_host(host)
        subprocess.run(['ping', host], check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}