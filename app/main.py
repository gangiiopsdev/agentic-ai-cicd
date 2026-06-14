from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    if host.startswith('127.0.0.1') or host.startswith('localhost'):
        args = ['ping', host]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'message': str(e)}
    else:
        return {'status': 'failed', 'message': 'Invalid host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.startswith('127.0.0.1') or host.startswith('localhost'):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'message': 'Invalid host'}