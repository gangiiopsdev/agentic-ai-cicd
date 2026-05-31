from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):\n\n    # Use the safe function\n    safe_ping(host)

    return {"status": "completed"}