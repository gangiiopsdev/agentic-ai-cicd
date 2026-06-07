from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1'] + [safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}