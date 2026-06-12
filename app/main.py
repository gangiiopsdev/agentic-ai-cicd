from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()

group ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)