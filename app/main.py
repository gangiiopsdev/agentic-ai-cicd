from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.call(args)
    return result

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = safe_ping(host)
    return {"status": "completed", "result": result}