from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize and escape the input
    safe_host = shlex.quote(host)

    # Secure implementation
    subprocess.call(["ping", safe_host])

    return {"status": "completed"}