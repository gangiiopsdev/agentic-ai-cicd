from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return safe_ping(host)
    else:
        return 'Invalid host input'