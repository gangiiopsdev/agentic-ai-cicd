from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

def ping(host: str):
    # Validate and escape input to prevent shell injection
    host = shlex.quote(host)
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}

global_app.add_api_route("/ping", ping, methods=["GET"])