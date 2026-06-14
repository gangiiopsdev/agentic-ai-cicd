from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    command = 'ping' + (' -c 1' if host.startswith('linux') else '') + f' {host}'
    output = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': output.stdout if not output.stderr else output.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)