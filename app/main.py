from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str) -> bool:
    if not host.isalnum():
        return False
    try:
        result = subprocess.run(['ping', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError('Invalid hostname')
    return {"status": "completed"}