from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input by escaping special characters and limiting length
            sanitized_host = ''.join(c if c.isalnum() else '_' for c in host[:255])
            args = ['ping', sanitized_host]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)