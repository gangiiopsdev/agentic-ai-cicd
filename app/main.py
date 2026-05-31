from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic here
    return host.isdigit()

@app.get("/ping")
def ping(host: str):

    if not is_valid_host(host):
        return {'status': 'invalid host'}

    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)

    return {'status': 'completed'}