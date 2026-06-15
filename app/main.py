from fastapi import FastAPI
import subprocess

app = FastAPI()

def allowed_ip(ip):
    return ip.startswith('192.168.') or ip.startswith('172.16.0.0/16')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if allowed_ip(host):
        subprocess.run(['ping', host], check=True, shell=False)
    else:
        return {'status': 'invalid host'}
    return {'status': 'completed'}