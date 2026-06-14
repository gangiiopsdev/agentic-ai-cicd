from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
def safe_ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', str(5), host], timeout=10, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)