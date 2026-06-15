from fastapi import FastAPI
import subprocess
cimport socket

def ping(host: str):
    try:
        ip = socket.gethostbyname(host)
        p = subprocess.Popen(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}
    except socket.gaierror:
        return {'status': 'failed', 'error': f'Invalid hostname: {host}'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    # Use shlex.quote to safely escape the user-provided input
    safe_host = shlex.quote(host)
    return ping(safe_host)