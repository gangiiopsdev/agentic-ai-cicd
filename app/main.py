from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)