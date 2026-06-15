from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host to ensure it is safe to use with ping
    if not host.strip() or any(char in host for char in [';', '&', '|', '`', '$', '*', '?']):
        raise ValueError('Invalid host name')
    generators = {
        'ping': lambda host: subprocess.run(['ping', host], capture_output=True, text=True)
    }

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout, 'stderr': result.stderr}
    except ValueError as e:
        return {'error': str(e)}