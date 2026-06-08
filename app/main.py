from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not os.path.exists('/usr/bin/ping') or host.find('/') != -1:
        return {'status': 'error', 'message': 'Invalid input'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}