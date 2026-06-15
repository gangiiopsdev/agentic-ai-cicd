from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        try:
            output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)