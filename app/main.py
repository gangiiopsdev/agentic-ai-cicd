from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = 'ping'
    args = shlex.split(cmd)
    if host:
        args.append(host)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}