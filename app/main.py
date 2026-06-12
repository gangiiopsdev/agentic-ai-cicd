from fastapi import FastAPI
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
    subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed"}