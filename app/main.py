from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}