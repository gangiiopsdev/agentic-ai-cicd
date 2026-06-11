from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not all(c in '0123456789.' for c in host) or '.' not in host:
        return {'status': 'error', 'output': 'Invalid host'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}