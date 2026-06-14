from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}