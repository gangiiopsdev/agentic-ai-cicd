from fastapi import FastAPI
import subprocess
import string

app = FastAPI()

def safe_ping(host: str):
    if host.strip() in ['localhost', '127.0.0.1']:
        try:
            output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
    else:
        return {'status': 'denied', 'message': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    if not all(c in string.digits + '.' + '-' for c in host) or any(char.isdigit() and int(char) > 255 for char in host.split('.')):
        return {'status': 'denied', 'message': 'Invalid host'}
    return safe_ping(host)