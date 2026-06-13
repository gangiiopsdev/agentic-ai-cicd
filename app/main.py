from fastapi import FastAPI, HTTPException
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail='Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    # Use a full path for the command to mitigate risks
    subprocess.run(['/bin/ping', '-c', '1', host], check=True)
    return {'status': 'completed'}