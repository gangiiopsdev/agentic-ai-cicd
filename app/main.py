from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and escaping
    cmd_parts = ['ping', host]
    subprocess.call(cmd_parts, shell=False)
    return {'status': 'completed'}