from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping_endpoint(host: str):
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        raise ValueError("Invalid hostname")
    return ping(host)