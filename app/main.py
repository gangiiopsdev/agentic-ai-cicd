from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    command = ["ping", "-c", "1", host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'result': result.stdout}