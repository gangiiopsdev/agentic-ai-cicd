from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(quote(['ping', host]), shell=False)
    return {"status": "completed"}