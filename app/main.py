from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 10

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        raise HTTPException(status_code=400, detail="Invalid host name")
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}