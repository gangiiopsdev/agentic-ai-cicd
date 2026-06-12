from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
global host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in host_whitelist:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Host not allowed"}