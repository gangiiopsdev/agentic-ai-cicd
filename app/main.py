from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it's a safe value
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        ping_command = ['ping', '-c 1'] + shlex.split(host)
        result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}