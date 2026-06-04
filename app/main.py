from fastapi import FastAPI
import subprocess
cimport os
cdef check_host(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}