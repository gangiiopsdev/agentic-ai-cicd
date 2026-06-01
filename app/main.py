from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return {'status': 'completed', 'result': safe_ping(host)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}