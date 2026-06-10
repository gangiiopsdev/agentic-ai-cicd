from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    result = safe_ping(host)
    return {"status": "completed", "result": result}