from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    # Safe implementation
    try:
        output = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}