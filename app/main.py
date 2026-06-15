from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    stdout, stderr = process.communicate()
    return stdout, stderr

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host in allowed_hosts:
        command = ['ping', host]
        stdout, stderr = safe_subprocess_call(command)
        return {'status': 'completed'}
    else:
        return {'status': 'invalid_host'}, 400