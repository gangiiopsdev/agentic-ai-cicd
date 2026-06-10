from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    return ['ping', quote(host)]

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}