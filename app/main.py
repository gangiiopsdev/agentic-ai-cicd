from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use a whitelist of allowed hosts for safety
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        result = subprocess.run(['ping', '--count=1', host], capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)