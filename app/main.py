from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/ping")
def ping_route(host: str):
    if host in ['127.0.0.1', '::1']:  # Restrict to localhost for security reasons
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}