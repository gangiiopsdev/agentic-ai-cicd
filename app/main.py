from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Ensure only allowed hostnames are used
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout, 'error': ''}