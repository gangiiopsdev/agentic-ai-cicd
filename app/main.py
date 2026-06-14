from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)