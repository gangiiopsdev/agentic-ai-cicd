from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation without shell=True
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Validate the input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)  # Validate the input before using it
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}