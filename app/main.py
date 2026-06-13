from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host to prevent injection
    if not host.isalnum() and '.' not in host:
        raise ValueError('Invalid host')
    # Sanitize input by escaping special characters
    sanitized_host = subprocess.list2cmdline([host])
    # Using subprocess.run with shell=False and list of arguments for security
    result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}