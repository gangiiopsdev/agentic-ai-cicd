from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list to avoid shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function instead of vulnerable implementation
    safe_ping(host)
    return {"status": "completed"}