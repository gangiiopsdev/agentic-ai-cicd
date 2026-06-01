from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

def safe_ping(host: str):
    if host.strip() in ALLOWED_HOSTS:
        try:
            output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
    else:
        return {'status': 'denied', 'message': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)