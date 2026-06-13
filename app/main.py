from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {'error': 'Invalid input'}
    return safe_ping(host)