from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_safe_host(host):
    # Implement a function to check if the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts