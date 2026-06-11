from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isdigit() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping'] + shlex.split('-c 4 ' + host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}