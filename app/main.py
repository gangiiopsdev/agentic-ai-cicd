from fastapi import FastAPI
import subprocess
cimport = { 'ping': 'ping' }

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        return {'error': 'Invalid host'}, 400
    # Use subprocess.run instead of subprocess.call to avoid shell injection
    result = subprocess.run([cimport[host], host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}