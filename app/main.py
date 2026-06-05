from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and using shlex to safely handle user input
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)