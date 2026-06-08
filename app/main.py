from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

@app.get('/ping')
async def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}