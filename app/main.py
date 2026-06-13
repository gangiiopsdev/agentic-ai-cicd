from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")

app = FastAPI()

@app.get="/ping"
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitize_host(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}