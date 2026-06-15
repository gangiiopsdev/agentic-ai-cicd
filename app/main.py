from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}