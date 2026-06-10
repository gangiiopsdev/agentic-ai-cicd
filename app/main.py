from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def secure_ping(host: str):
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}

@app.get="/ping")
def ping(host: str):
    return secure_ping(host)