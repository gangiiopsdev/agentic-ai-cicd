from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)