from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ["example.com", "another-example.com"]
    if host in allowed_hosts:
        return True
    return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", "-c", "1", '--'], check=True, shell=False)
    return {"status": "completed"}