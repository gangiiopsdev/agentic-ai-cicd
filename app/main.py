from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Add input validation to ensure 'host' is a valid hostname or IP address
    if not host.isalnum() and '.' not in host:
        raise ValueError('Invalid host name')
    return execute_ping(host)