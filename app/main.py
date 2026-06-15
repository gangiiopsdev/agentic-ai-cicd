from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize host input
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)