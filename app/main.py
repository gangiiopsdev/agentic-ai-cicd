from fastapi import FastAPI
import subprocess
def q(s):
    return s.replace(';', '')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter cannot be empty'}
    try:
        output = subprocess.check_output(['ping', q(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}