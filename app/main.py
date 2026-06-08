from fastapi import FastAPI
import subprocess

app = FastAPI()
host_list = ['example.com']

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        raise HTTPException(status_code=403, detail="Host not allowed")
    # Safe implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}