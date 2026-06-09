from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Safe implementation using subprocess.run and shlex.split
            args = ['ping', host]
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)