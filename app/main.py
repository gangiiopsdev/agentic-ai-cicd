from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Validate host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    ping_service = PingService()
    try:
        result = ping_service.ping(host)
        return {'status': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    except ValueError as e:
        return {'error': str(e)}