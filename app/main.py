from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}