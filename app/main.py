from fastapi import FastAPI
import subprocess
def safe_ping(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or '&&' in host or ';' in host:
        return {'status': 'failed', 'error': 'No valid host provided'}
    return safe_ping(['ping', host])