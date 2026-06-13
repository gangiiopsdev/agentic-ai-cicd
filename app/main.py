from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_host(host):
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.run(['ping', '-c', '1', f'-I {os.getenv('PRIMARY_INTERFACE', 'eth0')} {sanitized_host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}