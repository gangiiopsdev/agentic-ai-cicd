from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using Popen and passing args separately to avoid shell=True
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}