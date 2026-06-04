from fastapi import FastAPI
import subprocess
def execute_ping(host):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)