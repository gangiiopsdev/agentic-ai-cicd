from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Host is not allowed"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)