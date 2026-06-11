from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    service = PingService()
    return service.ping(host)