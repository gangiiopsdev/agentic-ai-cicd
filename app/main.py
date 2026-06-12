from fastapi import FastAPI
import subprocess

def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)