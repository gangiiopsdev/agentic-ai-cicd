from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex to prevent shell injection
    cmd_parts = ['ping', shlex.quote(host)]
    subprocess.call(cmd_parts)

    return {'status': 'completed'}