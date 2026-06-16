from fastapi import FastAPI
import subprocess
cimport os
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    cmd = ['ping', host]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed: {error.decode()}')
    return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping_wrapper():
    host = 'example.com'  # Replace with actual dynamic host input handling
    return ping(host)