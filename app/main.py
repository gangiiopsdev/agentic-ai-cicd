from fastapi import FastAPI
import subprocess
global host_list = ['127.0.0.1']
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in host_list:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}