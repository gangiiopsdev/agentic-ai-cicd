from fastapi import FastAPI
import re

class PingService:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        # Regular expression to validate the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)