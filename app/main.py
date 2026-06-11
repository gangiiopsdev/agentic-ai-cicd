from fastapi import FastAPI
import subprocess
import shlex
global allowed_hosts = ['google.com', 'bing.com']

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get("/ping")
def ping(host: str):
    try:
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Host not allowed'}
        sanitized_host = sanitize_input(host)
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}