from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isdigit() or len(host) > 3:
        raise ValueError('Invalid host value')
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)