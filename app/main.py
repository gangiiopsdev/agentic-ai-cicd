from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    return host and '.' in host