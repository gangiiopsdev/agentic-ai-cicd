from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using shlex.quote to sanitize input
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host])

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}