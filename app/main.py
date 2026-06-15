from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isdigit():
        return False
    args = ['ping', '-c', '4'] + shlex.split(host)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if not output:
        return {'error': error}
    return {'status': 'completed', 'output': output}