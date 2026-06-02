from fastapi import FastAPI
import subprocess
app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if host not in ['localhost', '127.0.0.1']:
        return {'status': 'failed', 'error': 'Invalid host'}
    else:
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}