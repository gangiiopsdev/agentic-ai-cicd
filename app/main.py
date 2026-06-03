from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation
        try:
            result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)