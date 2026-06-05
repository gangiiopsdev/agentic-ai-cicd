from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() and c.islower())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}