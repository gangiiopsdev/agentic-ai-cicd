from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    Ping.safe_ping(host)
    return {"status": "completed"}