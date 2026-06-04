from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host not in ['example.com', 'test.net']:
        raise ValueError("Unsafe host")
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}