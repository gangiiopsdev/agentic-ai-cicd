from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    if '.' not in host or not host.replace('.', '').isnumeric():
        raise ValueError('Invalid host format')
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}