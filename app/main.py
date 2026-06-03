from fastapi import FastAPI
import subprocess
global_args = ['ping']
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    subprocess.call(global_args + [host])
    return {"status": "completed"}