from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}