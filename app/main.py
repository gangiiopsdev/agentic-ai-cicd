from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', '1', str(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', str(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}