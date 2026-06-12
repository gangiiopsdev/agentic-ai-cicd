from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {'status': 'completed', 'output': output}