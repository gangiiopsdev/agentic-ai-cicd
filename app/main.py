from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(["ping", quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "output": result.stdout.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr.decode()
        }