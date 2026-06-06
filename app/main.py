from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.call(['ping', host])
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)