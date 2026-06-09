from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def check_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    check_host(host)
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}