from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return 'Ping timed out'
    except Exception as e:
        return f'Error: {e}

def safe_host_validation(host: str):
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid host address')

@app.get("/ping")
def ping(host: str):
    try:
        safe_host_validation(host)
        return {'status': 'completed', 'output': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400