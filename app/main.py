from fastapi import FastAPI
import subprocess

app = FastAPI()

def allowed_ip(ip):
    return ip.startswith('192.168.') or ip.startswith('172.16.0.0/16')

@app.get('/ping')
def ping(host: str):    
    if allowed_ip(host):
        try:
            subprocess.run(['ping', host], check=True, capture_output=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'invalid host'}