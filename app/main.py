from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed', 'message': 'Ping successful'}
    else:
        return {'status': 'failed', 'message': 'Ping failed'}