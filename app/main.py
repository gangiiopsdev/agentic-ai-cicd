from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}