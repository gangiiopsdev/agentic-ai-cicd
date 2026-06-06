from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)