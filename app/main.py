from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command_parts):
        subprocess.run(command_parts, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]
    SafeSubprocess.run(command_parts)
    return {"status": "completed"}