from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}