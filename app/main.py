from fastapi import FastAPI
import subprocess
global_hosts = set()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in global_hosts:
        global_hosts.add(host)
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
            return {"status": "completed", "output": result.stdout}
        except subprocess.TimeoutExpired:
            return {"status": "timeout"}
    return {"status": "host already checked"}