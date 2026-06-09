from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input and use subprocess.run with shell=False
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}