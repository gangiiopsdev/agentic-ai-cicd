from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add your logic to validate the host
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}