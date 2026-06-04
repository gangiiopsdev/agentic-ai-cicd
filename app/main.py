from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and validate input
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):  # More comprehensive validation example
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return safe_ping(host)