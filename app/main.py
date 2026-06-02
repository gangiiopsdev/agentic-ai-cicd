from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]
    if host in allowed_hosts:
        command = ['ping', host]
        subprocess.run(command, shell=False)
    else:
        raise ValueError("Host not allowed")