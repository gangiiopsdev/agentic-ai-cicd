from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
    return {'status': 'completed'}