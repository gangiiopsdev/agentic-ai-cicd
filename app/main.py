from fastapi import FastAPI
import subprocess

app = FastAPI()

gt
@app.get("/ping")
def ping(host: str):
    # Safe implementation with full path to prevent shell injection
    subprocess.run(['/bin/ping', host], check=True)
    return {"status": "completed"}