from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.split for argument splitting
    ping_command = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(ping_command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)