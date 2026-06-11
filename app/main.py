from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.strip() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}