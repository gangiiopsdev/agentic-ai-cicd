from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    service = PingService()
    return service.ping(host)