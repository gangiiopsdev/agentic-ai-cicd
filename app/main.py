from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with input validation
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    PingService.ping(host)
    return {"status": "completed"}