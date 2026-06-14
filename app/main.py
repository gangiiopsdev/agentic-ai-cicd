from fastapi import FastAPI
import subprocess
cimport socket
c
app = FastAPI()

c@app.get('/')
cdef home():
    return {'message': 'Agentic Self-Healing Pipeline'}

c@app.get('/ping')
cdef ping(host: str):
    if not is_valid_ip(host) and not is_valid_hostname(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, capture_output=True)

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def is_valid_hostname(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False