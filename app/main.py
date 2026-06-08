from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using safe method without shell=True
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)