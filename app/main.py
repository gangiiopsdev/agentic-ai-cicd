from fastapi import FastAPI
import subprocess
cimport shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}