from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def escape_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    command = ['ping', await escape_host(host)]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}