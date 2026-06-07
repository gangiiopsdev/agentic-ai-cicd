from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}