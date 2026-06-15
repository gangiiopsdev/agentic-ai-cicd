from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    try:
        result = subprocess.run(PingService().ping_command + [safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}