from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if not self.validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def validate_host(self, host: str) -> bool:
        # Implement validation logic here
        allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
        return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)