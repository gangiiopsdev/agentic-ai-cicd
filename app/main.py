from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', host):
        raise ValueError('Invalid IP address')
    subprocess.call(['ping', '-c', '1', host])

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}