from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using shlex.quote to sanitize input
    subprocess.call(['ping', quote(host)])

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}