from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        cmd = ["ping", host]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(["ping", host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e.stderr}'}, 400