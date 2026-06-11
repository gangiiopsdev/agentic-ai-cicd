from fastapi import FastAPI
import subprocess

global host_whitelist
host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

async def is_host_allowed(host):
    return host in host_whitelist

@app.get("/ping")
def ping(host: str):
    if not is_host_allowed(host):
        raise HTTPException(status_code=403, detail="Host not allowed")
    # Secure implementation
    subprocess.run(['ping', host], shell=False)
    return {"status": "completed"}