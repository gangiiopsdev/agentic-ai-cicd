from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['127.0.0.1', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}