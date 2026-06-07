from fastapi import FastAPI
import subprocess
from shlex import quote

def ping(host: str):
    try:
        output = subprocess.check_output([quote('ping'), quote(host)], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid input'}
    try:
        # Validate and sanitize the input further if necessary
        subprocess.run([quote('ping'), quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}