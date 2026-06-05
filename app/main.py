from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)