from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(["ping", "/sbin/ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to avoid command injection
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return safe_ping(host)
    else:
        return {"status": "failed", "error": "Invalid host format"}