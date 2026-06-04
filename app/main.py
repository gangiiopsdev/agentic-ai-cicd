from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safer implementation with proper command sanitization
    try:
        result = subprocess.run(shlex.split('ping -c 1 ' + host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Sanitize input to avoid injection vulnerabilities
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)