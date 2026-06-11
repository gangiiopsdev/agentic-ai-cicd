from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape user input
    subprocess.call(['ping', quote(host)])
    return {"status": "completed"}