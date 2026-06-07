from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip() not in ['127.0.0.1', '::1']:  # Allow only localhost for example purposes
        return {'status': 'denied'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)