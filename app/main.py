from fastapi import FastAPI
import subprocess
global allow_hosts = ['example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or '&&' in host or ';' in host or host not in allow_hosts:
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}