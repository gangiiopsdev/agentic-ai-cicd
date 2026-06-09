from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input using shlex.quote to prevent command injection
    sanitized_host = shlex.quote(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500

@app.get('/ping')
def ping(host: str):
    # Sanitize input using shlex.quote to prevent command injection
    sanitized_host = shlex.quote(host)
    return safe_ping(sanitized_host)