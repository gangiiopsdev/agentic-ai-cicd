from fastapi import FastAPI
import subprocess
global host_list = ['127.0.0.1']
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or host.startswith('-') or len(host) > 4:
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}