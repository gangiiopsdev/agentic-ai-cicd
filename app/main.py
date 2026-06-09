from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    args = ['ping', host]
    subprocess.run(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {"status": "completed"}