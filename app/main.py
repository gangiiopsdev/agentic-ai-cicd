from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}