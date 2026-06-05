from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)