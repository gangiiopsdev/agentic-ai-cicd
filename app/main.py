from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_trusted_host(host):
    return host in ['localhost', '127.0.0.1']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_trusted_host(host):
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Untrusted host'}, 403