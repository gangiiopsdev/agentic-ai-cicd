from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    subprocess.call(['ping', '-c', '1', host])

@app.get("/ping")
def ping(host: str):  
    safe_ping(host)
    return {"status": "completed"}