from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = quote(host)
    try:
        output = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}