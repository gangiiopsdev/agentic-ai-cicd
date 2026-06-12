from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}