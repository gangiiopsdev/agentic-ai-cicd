from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return shlex.quote(input_str)

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, text=True, capture_output=True)
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}