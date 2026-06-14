from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'invalid_input'}
    args = shlex.split(f"ping {host}")
    subprocess.Popen(args)
    return {'status': 'completed'}