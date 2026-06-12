from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Enhanced validation to include whitespace and other special characters
    if not re.match(r'^[a-zA-Z0-9- .]+$', host):
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    result = safe_ping(host)
    return {"status": "completed", "result": result}