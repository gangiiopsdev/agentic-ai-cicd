from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or ' ' in host or '\' in host or '/' in host or ';' in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    return safe_ping(host)