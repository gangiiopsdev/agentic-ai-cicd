from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400