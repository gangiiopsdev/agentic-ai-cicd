from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation without using shell=True
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr}

app = FastAPI()

@app.get="/ping")
def ping_route(host: str):
    return PingService.ping(host)