from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in (".", "-") for c in host)

@app.get("/ping/")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}