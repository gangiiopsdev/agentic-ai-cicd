from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Use a safe method without shell=True
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    # Call the safe function
    ping_safe(host)
    return {"status": "completed"}