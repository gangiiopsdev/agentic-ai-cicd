from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}