from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def secure_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str): 
    return secure_ping(host)