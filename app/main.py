from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.replace('.', '').isnumeric() or '.' not in host:
        raise ValueError('Invalid host format')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}