from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Implement proper sanitization logic here
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}