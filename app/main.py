from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    validate_host(host)
    response = safe_ping(host)
    return {"status": "completed", "response": response}