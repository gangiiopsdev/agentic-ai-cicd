from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}