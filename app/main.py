from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}