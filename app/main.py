from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_host_validation(host):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if safe_host_validation(host):
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    else:
        return {'status': 'error', 'message': 'Invalid host'}