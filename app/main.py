from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using a list instead of shell=True and validating host
    if validate_host(host):
        subprocess.call(['ping', host])
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    return host in allowed_hosts