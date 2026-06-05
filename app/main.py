from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation with shell=False and proper quoting of arguments
    try:
        output = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').replace('-', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    return secure_ping(host)