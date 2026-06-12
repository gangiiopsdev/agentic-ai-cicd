from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return SafePing.ping(host)