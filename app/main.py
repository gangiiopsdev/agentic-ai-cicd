from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not validate_host(host):
        return {'status': 'Invalid host'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str):
    # Implement validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts