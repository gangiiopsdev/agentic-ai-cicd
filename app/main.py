from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    args = ['ping', host]
    result = subprocess.call(args)
    return result

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "exit_code": status}