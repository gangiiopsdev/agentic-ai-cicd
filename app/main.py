from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum() or '@' in host:
        return {'error': 'Invalid hostname'}, 400

    # Secure implementation with proper validation and use of shlex.split for safe argument parsing
    subprocess.run(['ping', '-c', '1'] + shlex.split(host), check=True)

    return {'status': 'completed'}