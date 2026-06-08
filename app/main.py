from fastapi import FastAPI
import subprocess
cimport = None
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'status': 'error', 'error': 'Host parameter is required'}
    try:
        result = subprocess.check_output(['ping', '-c', '1', host], shell=False)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}