from fastapi import FastAPI
import subprocess
cimport os

def safe_ping(host: str) -> str:
    # Sanitize input to avoid shell injection
    sanitized_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)