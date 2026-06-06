from fastapi import FastAPI
import subprocess
import re

global ping_cmd
ping_cmd = ['ping', 'google.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and host == 'google.com':
        try:
            subprocess.run(ping_cmd, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': f'Ping failed with error: {e}'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}