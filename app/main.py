from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', 'localhost']
def safe_ping(host: str):
    if not any(host.startswith(allowed_host) for allowed_host in allowed_hosts):
        raise Exception('Host is not allowed')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)