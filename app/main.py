from fastapi import FastAPI
import subprocess
cimport os

hosts_to_ping = ['host1', 'host2'] # Replace with actual list of hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in hosts_to_ping:
        raise Exception('Invalid host')
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}