from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list of arguments
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)
return {"status": "completed"}