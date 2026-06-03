from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full command and shell=False
g    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    response = ping(host)
    return {"status": "completed"}