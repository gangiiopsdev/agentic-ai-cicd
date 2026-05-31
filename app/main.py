from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def secure_ping(host):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)