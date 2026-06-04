from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if not self.is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    def is_valid_host(self, host: str):
        # Add validation logic here to ensure the host is safe to ping
        return '.' in host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)