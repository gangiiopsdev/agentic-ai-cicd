from fastapi import FastAPI
import subprocess
def ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)