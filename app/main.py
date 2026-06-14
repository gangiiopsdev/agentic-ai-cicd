from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}