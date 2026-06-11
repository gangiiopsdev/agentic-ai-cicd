from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return f'ping {host}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(safe_ping(host).split(), check=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}