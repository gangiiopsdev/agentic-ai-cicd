from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shell=False and validate host input
    if not host.isalnum():
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Using safe_ping function with validation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}