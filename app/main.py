from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host not in ('127.0.0.1', 'localhost'):
        return {'error': 'Unauthorized ping attempt'}
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)