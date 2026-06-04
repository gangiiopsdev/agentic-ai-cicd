from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    response = execute_ping(host)
    return {'status': 'completed', 'output': response}