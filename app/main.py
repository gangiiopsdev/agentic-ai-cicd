from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}