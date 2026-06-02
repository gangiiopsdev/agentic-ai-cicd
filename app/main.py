from fastapi import FastAPI
import shlex
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        args = shlex.split(f"ping {host}")
        subprocess.call(['ping', *args])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}