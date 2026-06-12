from fastapi import FastAPI
import subprocess
good_hosts = ['127.0.0.1', '::ffff:127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in good_hosts:
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'denied', 'message': 'Host not allowed'}