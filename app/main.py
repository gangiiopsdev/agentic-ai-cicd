from fastapi import FastAPI
import subprocess
class HostValidator:
    @staticmethod
def validate(host: str) -> bool:
        allowed_hosts = {'example.com', 'test.com'}
        return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not HostValidator.validate(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}