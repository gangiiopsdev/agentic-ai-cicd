from fastapi import FastAPI
import subprocess
import shlex
global ALLOWED_HOSTS = {'google.com', 'example.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid input'}
    sanitized_host = shlex.quote(host)
    try:
        # Secure implementation
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}