from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    try:
        subprocess.call(args)
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": result}