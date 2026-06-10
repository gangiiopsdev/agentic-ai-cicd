from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in ALLOWED_HOSTS:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Host not allowed'}
    return {'status': 'completed'}