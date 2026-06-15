from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and passing arguments separately
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}