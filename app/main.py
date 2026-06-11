from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    return host in safe_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        try:
            subprocess.check_call(['ping', host], shell=False)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Unauthorized host'}