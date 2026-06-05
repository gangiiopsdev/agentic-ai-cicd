from fastapi import FastAPI
import subprocess
cfrom subprocess import Popen, PIPE

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.strip() not in ['localhost', '127.0.0.1']:  # Restrict hosts to known safe ones
        return {'status': 'error', 'message': 'Invalid host'}
    result = Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
    output, error = result.communicate()
    if result.returncode != 0:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed', 'output': output.decode()}