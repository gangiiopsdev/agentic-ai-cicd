from fastapi import FastAPI
import subprocess
import shlex
global host_list = ["google.com", "yahoo.com"]
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {"error": "Invalid host"}
    command = 'ping {}
'.format(shlex.quote(host))
    subprocess.call(command, shell=True)
    return {"status": "completed"}