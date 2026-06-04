from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent injection attacks
        if '&&' in host or ';' in host or '|' in host:
            return {'status': 'failed', 'error': 'Invalid characters in input'}
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)