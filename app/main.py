from fastapi import FastAPI
import shlex
import os

app = FastAPI()

def safe_ping(host):
    try:
        args = ["ping", host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not shlex.split(host) == [host]:  # Check for shell metacharacters or injection attempts
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)