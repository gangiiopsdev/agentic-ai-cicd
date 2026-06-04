from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation example: allow only alphanumerics and hyphens
    return host.isalnum() or '-' in host

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}