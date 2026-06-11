from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    if host == 'localhost':
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if _ping(host):
        result = subprocess.call(["ping", host])
        return {"status": "completed", "result": result}
    else:
        return {"status": "not allowed"}