from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(value):
    return value

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}