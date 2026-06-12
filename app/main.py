from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.get("/ping")
async def ping_endpoint(host: str):
    return {'stdout': ping(host)}