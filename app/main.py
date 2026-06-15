from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more valid hosts if needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)