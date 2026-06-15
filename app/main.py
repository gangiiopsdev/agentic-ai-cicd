from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(hostname):
    # Add logic to validate hostnames
    return hostname in ['example.com', 'another.example.com']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe hostname")
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}