from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Implement logic to check if the host is safe (e.g., whitelist of allowed hosts)
    return host in ['example.com', 'another-example.com']

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        command = ["ping", *shlex.split(host)]
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}