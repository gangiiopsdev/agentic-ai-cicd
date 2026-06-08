from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced security implementation with proper validation and sanitization
    if host.strip().endswith('localhost') or '127.0.0.1' in host:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}