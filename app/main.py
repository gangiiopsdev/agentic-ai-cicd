from fastapi import FastAPI
import subprocess
gl = ['ping', '-c', '1', '-W', '5']

app = FastAPI()

def safe_ping(host: str):
    gl[2] = host
    subprocess.call(gl)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}