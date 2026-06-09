from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Restrict allowed hosts for security
        return {'status': 'error', 'output': 'Unauthorized host'}
    return safe_ping(host)