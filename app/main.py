from fastapi import FastAPI
import subprocess
import shlex
global ping
ping = None
cmd_args = ['ping', '-c', '4']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    global ping
    if ping is None:
        args = cmd_args + [host]  # Limit the number of pings to avoid abuse
        ping = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {
        "status": "completed",
        "output": ping.stdout.decode('utf-8').strip(),
        "error": ping.stderr.decode('utf-8').strip()
    }