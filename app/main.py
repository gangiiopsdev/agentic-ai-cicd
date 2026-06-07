from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host to prevent injection attacks
    if not host.replace('.', '').isnumeric():
        raise ValueError('Invalid host format')
    command = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)