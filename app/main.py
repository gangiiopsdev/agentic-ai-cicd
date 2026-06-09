from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.Popen
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    SafePing.ping(host)
    return {"status": "completed"}