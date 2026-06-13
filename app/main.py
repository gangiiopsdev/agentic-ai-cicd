from fastapi import FastAPI
import subprocess
cimport = ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}