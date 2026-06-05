from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Safe implementation
    SafePing.safe_ping(host)\n    return {"status": "completed"}