from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c in '0123456789.' for c in host) or '.' not in host:
        return '', False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout, True

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output, is_valid_host = safe_ping(host)
    if not is_valid_host:
        return {'status': 'error', 'output': 'Invalid host'}
    return {'status': 'completed', 'output': output}