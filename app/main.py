from fastapi import FastAPI, HTTPException
import subprocess

global host
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

def validate_host(host: str) -> bool:
    # Simple validation to ensure host is a valid IP address
    import ipaddress
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False