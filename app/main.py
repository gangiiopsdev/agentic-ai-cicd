from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not host in allowed_hosts:
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}