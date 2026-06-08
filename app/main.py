from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}