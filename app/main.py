from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(c if c.isalnum() or c in "._-" else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        command = ["ping", shlex.quote(sanitized_host)]
        subprocess.run(command, check=True)  # Use subprocess.run for better security and control
    else:
        return {"error": "Invalid hostname"}
    return {"status": "completed"}