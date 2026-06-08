from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        raise Exception('Invalid host')

    return {'status': 'completed'}