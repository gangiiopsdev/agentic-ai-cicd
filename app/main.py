from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}