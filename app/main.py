from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    args = ['ping', *shlex.split(host)]
    subprocess.run(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {'status': 'completed'}