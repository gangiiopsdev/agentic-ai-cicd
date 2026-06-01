from fastapi import FastAPI
import subprocess
glue
app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Add appropriate validation and sanitization logic here
        return run_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}