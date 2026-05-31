from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    args = ['ping', host]
    for arg in args:
        if isinstance(arg, list):
            args.extend(arg)
        else:
            args.append(arg)
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Use the safe function
    safe_ping(host)

    return {"status": "completed"}