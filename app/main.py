from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_safe_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        raise Exception('Invalid host')