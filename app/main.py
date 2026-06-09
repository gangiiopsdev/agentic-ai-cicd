from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

cping_service = PingService()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return cping_service.ping(host)

def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust checks as needed
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)