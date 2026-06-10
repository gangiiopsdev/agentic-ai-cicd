from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.isalnum() or '.' not in host:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if sanitize_host(host):
        args = ['ping', f"{host}"]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}