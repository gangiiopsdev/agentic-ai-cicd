from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it is a valid IP address or hostname
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = safe_ping(host)
    return {"status": "completed", "result": result}

def validate_host(host: str) -> bool:
    import re
    # Regex pattern to match a valid IP address or hostname
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.){2}[0-9]{1,3}|[a-zA-Z0-9\.-]+$'
    return re.match(pattern, host) is not None