from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}