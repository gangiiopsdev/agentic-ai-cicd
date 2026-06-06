from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_safe_host(host: str) -> str:
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return host

@app.get("/ping")
def ping(host: str):
    safe_host = get_safe_host(host)
    subprocess.run(['ping', '-c 1', safe_host], check=True, shell=False)
    return {"status": "completed"}