from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}