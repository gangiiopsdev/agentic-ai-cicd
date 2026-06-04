from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Host not allowed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)