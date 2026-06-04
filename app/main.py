from fastapi import FastAPI
import subprocess
global host
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}