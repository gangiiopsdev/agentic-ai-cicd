from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    if host not in ('127.0.0.1', '::1'):  # Restrict to localhost addresses
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(host)