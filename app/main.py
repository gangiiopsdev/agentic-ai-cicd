from fastapi import FastAPI
import subprocess

allowed_hosts = ['8.8.8.8', '127.0.0.1']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(4), host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}