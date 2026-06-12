from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    command = ['ping', '-c', '5', host]  # Use -c for specifying the number of pings on Unix-like systems
    subprocess.run(command, check=True, timeout=5)
    return {'status': 'completed'}