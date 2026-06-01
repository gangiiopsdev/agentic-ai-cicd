from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation without shell=True
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}