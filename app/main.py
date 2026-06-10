from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Unauthorized host'}, 403
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}