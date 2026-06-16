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
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    else:
        return {"error": "Invalid host"}