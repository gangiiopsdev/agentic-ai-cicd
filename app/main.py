from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    return host

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', safe_ping(host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}