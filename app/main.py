from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(shlex.quote(host))  # Use shlex.quote to sanitize the input
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}