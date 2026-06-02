from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Define allowed hosts or implement additional checks
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized host'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)