from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Simple check for common unsafe characters
    return hostname.replace('.', '').isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError('Unsafe hostname provided')
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}