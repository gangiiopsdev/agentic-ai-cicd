from fastapi import FastAPI
import subprocess

cimport = subprocess.check_output

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = cimport(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}