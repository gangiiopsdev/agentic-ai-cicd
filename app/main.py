from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        try:
            output = subprocess.check_output([os.path.join('/bin', 'ping'), '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
    else:
        return {'status': 'denied', 'message': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    if host.strip() not in ['localhost', '127.0.0.1']:
        raise Exception('Invalid host')
    return safe_ping(host)