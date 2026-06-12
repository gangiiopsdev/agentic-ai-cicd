from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}