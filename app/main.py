from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input
        if host in ['allowed_host1', 'allowed_host2']:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Host not allowed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)