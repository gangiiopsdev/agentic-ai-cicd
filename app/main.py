from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and argument list
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}, 500

def validate_host(host: str):
    # Validate and sanitize the host input to prevent shell injection
    if not host.strip() or '/' in host:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str = Query(..., min_length=1)):
    try:
        validate_host(host)
        safe_ping(shlex.quote(host))
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400