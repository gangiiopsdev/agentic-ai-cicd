from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
    def ping(host: str):
        # Safer implementation using a whitelist
        valid_hosts = {'example.com', 'test.example.net'}  # Replace with actual allowed hosts
        if host not in valid_hosts:
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    valid_hosts = {'example.com', 'test.example.net'}  # Replace with actual allowed hosts
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return PingService.ping(host)