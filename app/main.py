from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail="Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}