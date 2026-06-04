from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}