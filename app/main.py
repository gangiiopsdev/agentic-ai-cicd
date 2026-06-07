from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure host is not malicious
    if not all(char.isalnum() or char in ['-', '.', '_'] for char in host):
        raise ValueError("Invalid hostname")

@app.get('/ping')
def ping(host: str):  
    validate_host(host)
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}