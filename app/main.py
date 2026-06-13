from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.startswith(('localhost', '127.0.0.1')):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Unsafe ping target')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}