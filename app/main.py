from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.strip().isalnum():
        return {"status": "invalid input"}
    try:
        args = shlex.split('ping -c 1 ' + host)
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": f'Ping failed: {e}'}
    return {"status": "completed"}

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)