from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(host)
    return run_ping(sanitized_host)