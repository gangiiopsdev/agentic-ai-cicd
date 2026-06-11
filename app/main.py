from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return 'Ping request timed out'
    except Exception as e:
        return f'An error occurred: {str(e)}'

def safe_ping_wrapper(host: str):
    if not host.isdigit():  # Basic validation to avoid command injection
        return {'error': 'Invalid input'}
    return safe_ping(host)

@app.get("/ping")
def ping(host: str):
    result = safe_ping_wrapper(host)
    return {'status': 'completed', 'result': result}