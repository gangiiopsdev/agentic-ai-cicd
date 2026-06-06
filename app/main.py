from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Validate host input to prevent command injection
            if not all(c.isalnum() or c in '-.' for c in host):
                raise ValueError('Invalid host name')
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    service = PingService()
    return service.ping(host)