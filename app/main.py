from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    response = PingService.ping(host)
    return {'status': 'completed', 'output': response}