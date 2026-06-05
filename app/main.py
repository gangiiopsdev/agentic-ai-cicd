from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric():
        subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}