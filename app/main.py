from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate the host to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    
@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}