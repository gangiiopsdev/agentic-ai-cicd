from fastapi import FastAPI
import socket
cimport subprocess

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        subprocess.call(['ping', '-c', '1', ip_address], shell=False)  # Use shell=False to prevent command injection
    except socket.gaierror:
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    return {'status': 'completed'}