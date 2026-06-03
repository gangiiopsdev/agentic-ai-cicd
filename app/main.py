from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '-' in host or '.' in host:
        raise ValueError('Invalid input')
    args = ['ping', f'-c 1 {host}']
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}