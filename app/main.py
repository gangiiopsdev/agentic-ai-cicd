from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}