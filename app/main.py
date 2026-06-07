from fastapi import FastAPI
import subprocess
class PingService:
    def escape_host(self, host: str):
        return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    escaped_host = ping_service.escape_host(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}