from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Use subprocess.run with a safe list of arguments
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    service = PingService()
    return {'status': 'completed', 'result': service.ping(host)}