from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Validate and sanitize the input to prevent command injection
            if not host.isalnum():
                return {'status': 'failed', 'error': 'Invalid input'}
            output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)