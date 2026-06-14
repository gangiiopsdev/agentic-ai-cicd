from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get="/ping"
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}