from fastapi import FastAPI
import subprocess
cimport = {'ping': '/bin/ping'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with validation
    if not host.strip().isalnum() or len(host) > 255:
        return {'error': 'Invalid input'}, 400
    try:
        result = subprocess.run([cimport['ping'], f'-c {len(host)}', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500