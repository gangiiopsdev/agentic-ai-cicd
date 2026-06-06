from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            # Use the full path to 'ping' and ensure it's not from an untrusted source
            subprocess.run(['/usr/bin/ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)