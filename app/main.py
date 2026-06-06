from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    valid_hosts = ['localhost', '127.0.0.1']
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    else:
        result = run_ping(host)
        return result