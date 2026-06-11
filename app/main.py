from fastapi import FastAPI
import os
import shlex
def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return 'Invalid hostname'
    try:
        args = ['ping', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}