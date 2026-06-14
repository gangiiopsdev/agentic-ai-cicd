from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}