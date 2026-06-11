from fastapi import FastAPI
import subprocess
global ping

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(["ping", host])

return {"status": "completed"}