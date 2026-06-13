from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    command = ['ping', *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {"status": safe_ping(host)}