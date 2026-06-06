from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    subprocess.run(['ping', host], check=True)

c
@app.get("/ping")
def ping(host: str):

    safe_ping(host)

    return {"status": "completed"}