from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Input validation and escaping
    if not host.isalnum() or len(host) > 10:
        raise ValueError('Invalid input')
    args = ['ping', '-c', '1', host]  # Use '-c' to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400