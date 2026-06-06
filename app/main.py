from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '-c', '1', host]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.safe_ping(host)