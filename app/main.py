from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_safe_command(host):
    if not host.isdigit():
        return None
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    command = get_safe_command(host)
    if command:
        subprocess.run(command, shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}