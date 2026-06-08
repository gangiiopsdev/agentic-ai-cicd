from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def sanitize_host(host):
    # Implement proper input validation and sanitization
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_host(host))
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}