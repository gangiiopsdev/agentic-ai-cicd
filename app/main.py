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
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Use the safe function
    try:
        safe_ping(host)
        return {"status": "completed", "result": "success"}
    except Exception as e:
        return {"status": "failed", "result": str(e)}