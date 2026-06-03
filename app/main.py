from fastapi import FastAPI
import subprocess
class HostValidator:
    allowed_hosts = ['google.com', 'bing.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in HostValidator.allowed_hosts:
        return {"status": "failed", "error": "Host not allowed"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}