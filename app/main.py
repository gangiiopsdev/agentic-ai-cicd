from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'localhost' in host or '127.0.0.1' in host:
        args = ['ping', host]
        subprocess.call(args, shell=False)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}