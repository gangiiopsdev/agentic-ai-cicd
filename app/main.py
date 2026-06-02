from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_service = PingService()
    return ping_service.ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    return host in allowed_hosts