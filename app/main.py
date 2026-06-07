from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        try:
            # Escape user input to prevent shell injection
            args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
            result = subprocess.run(args, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)