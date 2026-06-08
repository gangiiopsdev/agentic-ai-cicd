from fastapi import FastAPI
import subprocess

def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

def validate_host(host):
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    result = execute_ping(host)
    if result['status'] == 'completed':
        return result
    else:
        return {'status': 'error', 'output': result['output']}