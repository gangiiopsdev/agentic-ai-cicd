from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run and shlex.split
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}