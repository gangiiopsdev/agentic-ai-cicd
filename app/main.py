from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    try:
        safe_ping(host)
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)"