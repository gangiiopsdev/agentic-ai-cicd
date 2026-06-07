from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts