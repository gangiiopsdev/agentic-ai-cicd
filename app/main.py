from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip().replace('.', '').isnumeric():
        raise ValueError('Invalid host address')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}