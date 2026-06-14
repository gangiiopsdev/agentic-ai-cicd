from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = ''.join(c for c in host if c.isalnum() or c in '_.')
    command = shlex.split(f'ping {safe_host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}