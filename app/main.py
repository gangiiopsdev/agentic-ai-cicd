from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return {'status': 'completed', 'result': safe_ping(host)}