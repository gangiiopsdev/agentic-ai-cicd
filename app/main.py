from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote
class SafePing:
    @staticmethod
def safe_ping(host: str):
        command = ['ping', host]
        result = subprocess.run(command, shell=False, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)