from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return host.strip() if host else ''

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid input"}
    command = ["ping", shlex.quote(sanitized_host)]
    subprocess.run(command)
    return {"status": "completed"}