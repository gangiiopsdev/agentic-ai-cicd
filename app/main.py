from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize the host input to prevent command injection
        safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
        try:
            result = subprocess.run(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return PingService.ping(host)