from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the input to prevent command injection
        if not host.strip() or '&&' in host or ';' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            result = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    return PingService.ping(host)