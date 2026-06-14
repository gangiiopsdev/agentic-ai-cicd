from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    output = safe_ping(host)\n    return {'status': 'completed', 'output': output}