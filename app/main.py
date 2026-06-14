from fastapi import FastAPI
import socket

app = FastAPI()

def validate_host(host: str):
    # Regular expression for validating a Hostname/IP
    regex = r'^[a-zA-Z0-9.-]+$'
    if not re.match(regex, host):
        return False
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    return True

def safe_ping(host: str):
    # Safe implementation using socket to ping a host
    try:
        response = socket.create_connection((host, 80), 2)
        response.close()
        return {'status': 'completed', 'message': 'Host is reachable'}
    except socket.error as e:
        return {'status': 'failed', 'message': str(e)}, 500

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    result = safe_ping(host)
    return result