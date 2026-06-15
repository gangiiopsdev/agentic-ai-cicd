from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isdigit() or int(host) < 1 or int(host) > 254:
        return {'error': 'Invalid host'}

    # Use subprocess.run with list of arguments to avoid shell=True and ensure proper sanitization
    result = subprocess.run(['ping', '-c', '4', str(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        return {'error': result.stderr.decode()}
    return {'status': 'completed'}