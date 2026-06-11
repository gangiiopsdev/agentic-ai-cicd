from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()
cping_service = PingService()

@app.get("/ping")
def ping(host: str):
    if not host.isdigit() and len(host) > 32:
        return {'status': 'failed', 'error': 'Invalid input'}
    return cping_service.ping(host)