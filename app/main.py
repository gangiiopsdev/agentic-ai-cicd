from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        # Sanitize host input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)