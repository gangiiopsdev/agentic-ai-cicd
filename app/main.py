from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ['127.0.0.1', '::1']
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in host_list:
        safe_host = shlex.quote(host)
        result = subprocess.call(f"ping {safe_host}", shell=False)
        return {"status": "completed", "result": result}
    else:
        return {"error": "Invalid host"}