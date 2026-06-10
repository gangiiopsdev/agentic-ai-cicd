from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in '._-' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    return run_ping(host)