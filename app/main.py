from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Simple validation to allow only alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise ValueError("Invalid host")

@app.get="/ping")
def ping(host: str):
    validate_host(host)
    result = safe_ping(host)
    return {"status": "completed", "result": result}