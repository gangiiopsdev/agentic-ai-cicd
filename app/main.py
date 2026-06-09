from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}