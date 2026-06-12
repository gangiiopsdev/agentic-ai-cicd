from fastapi import FastAPI
import subprocess
def validate_host(host):
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}