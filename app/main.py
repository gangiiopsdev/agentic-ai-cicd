from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using list of arguments instead of shell=True
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}