from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it's safe for the ping command
    allowed_hosts = ['example.com', 'test.example.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}

    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}