from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()} 
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)