from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}, 400

    # Secure implementation using shlex to safely split the command
    safe_host = shlex.quote(host)
    subprocess.run(["ping", safe_host], check=True)

    return {"status": "completed"}