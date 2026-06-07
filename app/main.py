from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "output": subprocess.check_output(['ping', host], text=True)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}