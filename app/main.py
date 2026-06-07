from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

@app.get("/ping")
def ping_handler(host: str):
    if 'localhost' not in host:
        return {'error': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}