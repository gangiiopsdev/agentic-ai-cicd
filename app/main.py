from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def _ping(host):
    args = [shlex.quote(arg) for arg in ['ping', host]]
    return args

@app.get("/ping")
def ping(host: str):
    try:
        args = _ping(host)
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}