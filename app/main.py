from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {'status': 'completed', 'stdout': result.stdout}