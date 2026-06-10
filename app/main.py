from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)