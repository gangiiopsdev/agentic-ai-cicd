from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent open redirect vulnerabilities
    if not host.startswith('http://') and not host.startswith('https://'):
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid input'}, 400