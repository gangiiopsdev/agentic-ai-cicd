from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    args = ['ping', subprocess.escape(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}