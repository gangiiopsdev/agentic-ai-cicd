from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input
    args = ['ping', '-c', '1', shlex.quote(host)]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}