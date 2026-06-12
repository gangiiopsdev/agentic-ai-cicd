from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']  # Allow only trusted hosts
    if host in allowed_hosts:
        try:
            output = subprocess.run(['ping', '-c', '4', '--host', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Untrusted host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)