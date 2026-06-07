from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize the host input
            if not all(c.isalnum() or c in '-.' for c in host):
                raise ValueError('Invalid hostname')
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    return PingService.ping(host)