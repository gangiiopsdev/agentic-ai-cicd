from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host not allowed')
    status = execute_ping(host)
    return {"status": "completed", "output": status}

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more hosts as needed
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')