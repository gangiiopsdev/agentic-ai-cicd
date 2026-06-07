from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)