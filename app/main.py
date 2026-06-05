from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host or len(host) > 100:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except (ValueError, subprocess.CalledProcessError) as e:
        return {'status': 'failed', 'error': str(e)}