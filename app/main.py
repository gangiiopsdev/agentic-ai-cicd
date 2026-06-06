from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    if not host:
        return False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = run_ping(host)
    return {"status": "completed", "output": status}