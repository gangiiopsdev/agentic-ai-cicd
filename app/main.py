from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shell=False and safely pass arguments
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "output": subprocess.run(['ping', host], check=True, capture_output=True, text=True).stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}