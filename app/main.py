from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safe call to the function above
    safe_ping(host)
    return {"status": "completed"}