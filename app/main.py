from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Use safe implementation with shlex.quote for user-supplied input
    safe_command = 'ping ' + shlex.quote(host)
    subprocess.run(safe_command, shell=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)