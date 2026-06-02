from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    return all(c.isalnum() or c in ('.', '-') for c in hostname)

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError('Unsafe hostname')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}