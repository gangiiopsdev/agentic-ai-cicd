from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)