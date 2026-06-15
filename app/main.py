from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}