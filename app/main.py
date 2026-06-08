from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

def validate_host(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return safe_ping(host)