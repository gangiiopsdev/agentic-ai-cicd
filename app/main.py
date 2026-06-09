from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced security implementation with proper validation and sanitization
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and (host.strip().endswith('localhost') or '127.0.0.1' in host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}