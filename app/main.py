from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host == 'localhost' or host == '127.0.0.1':
        return subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}