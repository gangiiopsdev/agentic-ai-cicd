from fastapi import FastAPI, HTTPException
import subprocess
import shlex

class CommandSanitizer:
    @staticmethod
def sanitize(command):
        return shlex.split(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host name")
    command = CommandSanitizer.sanitize(f'ping {host}')
    try:
        subprocess.run(command, shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}