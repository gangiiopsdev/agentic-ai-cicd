from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Validate and sanitize input
        if not self.is_valid_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

    def is_valid_host(self, host: str) -> bool:
        # Simple validation example
        return '.' in host and len(host.split('.')) == 4

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    try:
        return {'status': 'completed', 'output': ping_service.ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400