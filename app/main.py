from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '@' in host or '>' in host:
        raise ValueError('Unsafe input detected')
    subprocess.run(['ping', '-c 1', host], check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)