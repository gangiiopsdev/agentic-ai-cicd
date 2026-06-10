from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = shlex.quote(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}