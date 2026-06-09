from fastapi import FastAPI
import subprocess
import shlex

global_vars = globals()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in global_vars:
        try:
            # Secure implementation using subprocess.run with shell=False and arguments unpacking
            subprocess.run(shlex.split('ping ' + host), check=True)
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    return {"status": "completed"}