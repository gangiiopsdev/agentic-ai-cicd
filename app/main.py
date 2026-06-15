from fastapi import FastAPI
import subprocess
import re

allowed_hosts = ['example.com', 'another.example.com']

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Invalid host format')
    # Use a full path for the subprocess to mitigate risks
    result = subprocess.run(['/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Invalid host format')
    return safe_ping(host)