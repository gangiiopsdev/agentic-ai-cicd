from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return {"status": "completed"}