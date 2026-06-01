from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        if response:
            return {"status": "completed", "response": response}
        else:
            return {"status": "error", "message": "Invalid host"}
    except Exception as e:
        return {"status": "error", "message": str(e)}