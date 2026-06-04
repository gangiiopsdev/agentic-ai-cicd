from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

    try:
        subprocess.check_call(['ping', host], timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)