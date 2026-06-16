from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)