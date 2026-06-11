from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):  
    if not validate_host(host):
        return {'status': 'invalid host'}
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}

def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['127.0.0.1', '::1']
    for allowed_host in allowed_hosts:
        if allowed_host in host:
            return True
    return False