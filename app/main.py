from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'another.example.com']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}