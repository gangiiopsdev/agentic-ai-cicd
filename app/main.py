from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host input'}
    try:
        # Secure implementation using subprocess.run with validation and escaping
        command = ['ping', '-c', '1', shlex.quote(host)]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}