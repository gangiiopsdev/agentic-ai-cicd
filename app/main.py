from fastapi import FastAPI
import subprocess
global args
args = {"host": None}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global args
    args["host"] = host
    return {"status": "completed"}

@app.on_event("startup")
def startup_event():
    subprocess.call(f'ping {args["host"]}', shell=True)