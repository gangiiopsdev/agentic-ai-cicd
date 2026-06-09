from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation
    if host.startswith('-c 4') or host.startswith('--count=4'):
        return False
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return True

@app.get("/ping")
def ping(host: str):
    if secure_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid input detected."}