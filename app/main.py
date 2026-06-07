from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', *shlex.split(host)], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)