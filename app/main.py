from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = {'example.com', 'test.com'}

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unsafe host'}
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}