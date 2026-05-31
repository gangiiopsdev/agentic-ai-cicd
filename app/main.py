from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = f'ping {host}'
    result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}