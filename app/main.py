from fastapi import FastAPI
import subprocess
def is_safe_hostname(host):
    return host and all(char.isalnum() or char in [".", "-"] for char in host)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if is_safe_hostname(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    return {'status': 'invalid hostname'}