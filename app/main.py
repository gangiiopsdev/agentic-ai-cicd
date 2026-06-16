from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced implementation
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.strip()}
    return {'status': 'completed', 'output': result}