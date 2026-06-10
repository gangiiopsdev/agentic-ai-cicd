from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str):
        args = shlex.split(command)
        subprocess.run(args, check=True)
app = FastAPI()
def ping(host: str):
    # Secure implementation
    command = f'ping {host}'
    SafeSubprocess.call(command)
@app.get("/ping")
def ping_route(host: str):
    return ping(host)