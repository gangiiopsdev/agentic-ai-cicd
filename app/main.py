from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        command = shlex.split(f'ping {host}')
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)