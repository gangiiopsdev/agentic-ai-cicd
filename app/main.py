from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    safe_args = [shlex.quote(arg) for arg in args]
    subprocess.call(safe_args)
    return {"status": "completed"}