from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}