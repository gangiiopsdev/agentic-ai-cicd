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
    subprocess.call(['ping', '-c', '1', host], shell=False)  # Use specific arguments to mitigate risks
    return {'status': 'completed'}