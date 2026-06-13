from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}