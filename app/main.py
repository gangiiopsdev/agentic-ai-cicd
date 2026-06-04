from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        if not host.strip() or not host.strip().replace('.', '').isdigit():
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
ping_service = PingService()

@app.post('/ping/')
def ping_endpoint(host: str):
    return ping_service.ping(host)