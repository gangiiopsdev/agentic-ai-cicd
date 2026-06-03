from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    try:
        sanitized_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)