from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str): return ping(host)