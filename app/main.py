from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if ' ' in host or '&' in host or ';' in host:
        raise ValueError('Invalid input')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'message': 'Ping successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)