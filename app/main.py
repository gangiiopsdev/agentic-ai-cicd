from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)