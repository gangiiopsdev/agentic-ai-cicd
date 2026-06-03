from fastapi import FastAPI
import subprocess
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)