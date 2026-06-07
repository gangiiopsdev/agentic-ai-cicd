from fastapi import FastAPI
import subprocess
class PingHandler:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingHandler.safe_ping(host)