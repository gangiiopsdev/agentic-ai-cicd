from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to safely escape user input
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}