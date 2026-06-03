from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', quote(host)])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)