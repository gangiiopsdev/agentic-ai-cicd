from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def valid_host(host):
    # Add logic to validate the host, e.g., checking for allowed domains or IP ranges
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return True

@app.get("/ping")
def ping(host: str):
    valid_host(host)
    result = safe_ping(host)
    return {"status": "completed", "result": result}