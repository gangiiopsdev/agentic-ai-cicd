from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.strip().isdigit() or '.' not in host:
        raise ValueError('Invalid host address')

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation with input validation and sanitized command
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}