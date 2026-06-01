from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}