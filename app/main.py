from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Validate and sanitize the host input
            if not self.is_valid_host(host):
                raise ValueError('Invalid host')
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic here, e.g., check if the host is a valid IP address or domain name
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)