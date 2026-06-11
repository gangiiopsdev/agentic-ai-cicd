from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.strip() or '&&' in host or ';' in host or '|' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        # Use a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'localhost']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}