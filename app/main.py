from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping request timed out'}

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)