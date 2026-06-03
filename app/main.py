from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return 'Invalid hostname'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return safe_ping(host)