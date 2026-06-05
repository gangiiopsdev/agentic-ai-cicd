from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    output = subprocess.run(args, stderr=subprocess.STDOUT, capture_output=True, text=True)
    return {"status": "completed", "output": output.stdout}