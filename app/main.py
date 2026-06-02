from fastapi import FastAPI
import subprocess
import shlex

global ALLOWED_HOSTS = ['example.com', 'localhost']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}