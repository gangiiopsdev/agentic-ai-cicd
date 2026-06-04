from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Host not allowed"}