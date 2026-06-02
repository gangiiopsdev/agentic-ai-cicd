from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with argument quoting
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {"status": "completed"}